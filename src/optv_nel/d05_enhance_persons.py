import json
import os
import sys

#add project root to path so I can import a module from the wikidata folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))
import abgeordnetenwatch.client as abgeordnetenwatch_client
from abgeordnetenwatch.mappings import convert_to_wikidata_faction_id
from abgeordnetenwatch.mappings import convert_to_wikidata_party_id
from wikimedia_commons.helpers import extract_image_license

#Deduce the PARLIAMENTS from the filenames in the /persons folder
INPUT_DIR = 'data/03_deduped/persons/'
INPUT_FILES = [f for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, f))]
OUTPUT_DIR = 'data/05_enhanced/persons/'
PARLIAMENTS = [f.split('.json')[0] for f in INPUT_FILES]
print(PARLIAMENTS)

def add_faction_from_abgeordnetenwatch(abgeordnetenwatch_id, entry, parliament):
    faction = abgeordnetenwatch_client.get_faction(abgeordnetenwatch_id, parliament)
    if faction is not None:
        #Note: This overwrites a previously existing factionID from Wikidata.
        entry['factionID'] = convert_to_wikidata_faction_id(faction, parliament)
    return entry

def add_party_from_abgeordnetenwatch(abgeordnetenwatch_id, entry):
    party = abgeordnetenwatch_client.get_party(abgeordnetenwatch_id)
    if party is not None:
        print(party)
        #Note: This overwrites a previously existing partyID from Wikidata.
        entry['partyID'] = convert_to_wikidata_party_id(party)
    return entry

def process_file(infile_path, outfile_path, parliament):
    with open(infile_path) as infile:
        data = json.load(infile)
        result = []
        counter = 0
        for entry in data:
            print(counter, "ID:", entry['id'])
            if isinstance(entry.get("additionalInformation"), list):
                #TODO: Deal with edgecase that additionalInformation is a list and not a single object (just 1 occurance of this edge case right now)
                pass
            else:
                abgeordnetenwatch_id = entry.get("additionalInformation").get("abgeordnetenwatchID")
                print(abgeordnetenwatch_id)
                if abgeordnetenwatch_id is not None:
                    add_faction_from_abgeordnetenwatch(abgeordnetenwatch_id, entry, parliament)
                    add_party_from_abgeordnetenwatch(abgeordnetenwatch_id, entry)

            #Add thumbnailCreator and thumbnailLicense from Wikimedia Commons
            thumbnail_uri = entry.get("thumbnailURI")
            if thumbnail_uri is not None:
                license_info = extract_image_license(thumbnail_uri)
                entry['thumbnailCreator'] = license_info['creator']
                entry['thumbnailLicense'] = license_info['license']

            result.append(entry)
            counter = counter + 1
        with open(outfile_path, 'w', encoding='utf8') as outfile:
            json.dump(result, outfile, ensure_ascii=False)

for PARLIAMENT in PARLIAMENTS:
    infile = INPUT_DIR + PARLIAMENT+ '.json'
    outfile = OUTPUT_DIR + PARLIAMENT+ '.json'
    print(PARLIAMENT)
    process_file(infile, outfile, PARLIAMENT)