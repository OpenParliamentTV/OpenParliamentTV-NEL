from pathlib import Path
import json
from optv_nel.wikidata.manual_data import FACTION_SHORT_NAMES

INFILE = "data/03_deduped/factions/factions.json"
OUTPATH = Path("data/05_enhanced/factions")
OUTPATH.mkdir(parents=True, exist_ok=True)
OUTFILE = "factions.json"

def add_shortname(faction):
    if faction['id'] in FACTION_SHORT_NAMES:
        faction['labelAlternative'] = FACTION_SHORT_NAMES[faction['id']]
    return faction

with open(INFILE) as infile:
    data = json.load(infile)
    entries = [add_shortname(faction) for faction in data]
    entries.append({
        'type': 'faction', 
        'id': 'Q4316268', 
        'label': 'fraktionslos',
        'socialMediaIDs': [],
        'thumbnailURI': '',
        'abstract': 'fraktionslose Abgeordnete',
        'websiteURI': '',
        'labelAlternative': 'fraktionslos'
    })
    with open(OUTPATH / OUTFILE, 'w', encoding='utf8') as outfile:
        json.dump(entries, outfile, ensure_ascii=False)
        

