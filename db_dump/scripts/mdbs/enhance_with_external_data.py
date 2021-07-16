import json
import os
import sys

#add project root to path so I can import a module from the wikidata folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))
import abgeordnetenwatch.client as abgeordnetenwatch_client
from abgeordnetenwatch.mappings import convert_to_wikidata_faction_id

INFILE = './db_dump/data/mdbs/mdbs-deduped.json'
OUTFILE = './db_dump/data/mdbs/mdbs-final.json'

with open(INFILE) as infile:
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
                faction = abgeordnetenwatch_client.get_faction(abgeordnetenwatch_id)
                if faction is not None:
                    faction_label = faction.get('fraction').get('label')
                    #Add factionID from abgeordnetenwatch. Note: This overwrites a previously existing factionID from Wikidata.
                    entry['factionID'] = convert_to_wikidata_faction_id(faction_label)
        result.append(entry)
        counter = counter + 1
    with open(OUTFILE, 'w', encoding='utf8') as outfile:
            json.dump(result, outfile, ensure_ascii=False)
