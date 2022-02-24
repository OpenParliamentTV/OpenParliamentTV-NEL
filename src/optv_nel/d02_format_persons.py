from pathlib import Path
import json
import os
import optv_nel.helpers as helpers

#Deduce the PARLIAMENTS from the filenames in the /persons folder
INPUT_DIR = "data/01_raw/persons"
OUTPUT_DIR = Path("data/02_formatted/persons")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
INPUT_FILES = [f for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, f))]
PARLIAMENTS = [f.split('.json')[0] for f in INPUT_FILES if '_extra' not in f]
print(PARLIAMENTS)

def reformat(obj, person_type):
    flat = {key : value['value'] for (key, value) in obj.items()}
    id = flat.pop('person').split('/')[-1]
    label = flat.pop('personLabel')
    birthDate = None
    if 'dateOfBirth' in flat:
        birthDate = flat.pop('dateOfBirth', None).replace('T00:00:00Z', '')
    partyID = flat.pop('party', '').split('/')[-1]
    factionID = flat.pop('faction', '').split('/')[-1]
    new = {
        'type': person_type, 
        'id': id, 
        'label': label, 
        'birthDate': birthDate,
        'partyID': partyID if len(partyID)>0 else None,
        'factionID': factionID if len(factionID)>0 else None,
        'socialMediaIDs': helpers.group_socials(flat),
        'additionalInformation': helpers.group_additional_information(flat),
        **flat
    }
    return new

for PARLIAMENT in PARLIAMENTS:
    INFILE = Path(INPUT_DIR) / Path(PARLIAMENT + ".json")
    OUTFILE = OUTPUT_DIR / Path(PARLIAMENT + ".json")
    with open(INFILE) as infile:
        data = json.load(infile)
        entries = [reformat(entry, "memberOfParliament") for entry in data['results']['bindings']]
        #check if there is an "extra" file to merge in...
        extra_file = PARLIAMENT + '_extra.json'
        if extra_file in INPUT_FILES:
            with open(INPUT_DIR / Path(extra_file)) as infile:
                extra_data = json.load(infile)
                extra_entries = [reformat(entry, 'otherSpeaker') for entry in extra_data['results']['bindings']]
                entries = entries + extra_entries
        with open(OUTFILE, 'w', encoding='utf8') as outfile:
            json.dump(entries, outfile, ensure_ascii=False)