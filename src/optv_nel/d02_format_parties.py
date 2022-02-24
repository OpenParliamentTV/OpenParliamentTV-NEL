from pathlib import Path
import json
import optv_nel.helpers as helpers

INFILE = "data/01_raw/parties/parties.json"
OUTPATH = Path("data/02_formatted/parties")
OUTPATH.mkdir(parents=True, exist_ok=True)
OUTFILE = OUTPATH / Path("parties.json")

def reformat(obj):
    flat = {key : value['value'] for (key, value) in obj.items()}
    id = flat.pop('ppg').split('/')[-1]
    label = flat.pop('ppgLabel')
    new = {
        'type': 'party', 
        'id': id, 
        'label': label,
        'socialMediaIDs': helpers.group_socials(flat),
        **flat
    }
    return new

# map over the entries and reformat each of them (reformatting means changing property names or grouping properties)
with open(INFILE) as infile:
    data = json.load(infile)
    entries = [reformat(entry) for entry in data['results']['bindings']]
    helpers.check_for_dups(entries)
    with open(OUTFILE, 'w', encoding="utf8") as outfile:
        json.dump(entries, outfile, ensure_ascii=False)

