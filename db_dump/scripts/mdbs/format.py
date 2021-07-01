import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import helpers


INFILE = 'db_dump/data/mdbs/mdbs-rawqueryresults.json'
OUTFILE = 'db_dump/data/mdbs/mdbs-formatted.json'

def reformat(obj):
    flat = {key : value['value'] for (key, value) in obj.items()}
    id = flat.pop('mdb').split('/')[-1]
    label = flat.pop('mdbLabel')
    birthDate = flat.pop('dateOfBirth', None).replace('T00:00:00Z', '')
    partyID = flat.pop('party', '').split('/')[-1]
    factionID = flat.pop('faction', '').split('/')[-1]
    new = {
        'type': 'memberOfParliament', 
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


# map over the entries and reformat each of them (reformatting means changing property names or grouping properties)
with open(INFILE) as infile:
    data = json.load(infile)
    entries = [reformat(entry) for entry in data['results']['bindings']]
    for e in entries:
        print(json.dumps(e, indent=4, sort_keys=True))
    with open(OUTFILE, 'w', encoding='utf8') as outfile:
        json.dump(entries, outfile, ensure_ascii=False)
