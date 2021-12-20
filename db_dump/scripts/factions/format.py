import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import helpers

INFILE_BUNDESTAG = 'db_dump/data/factions/factions-bundestag-rawqueryresults.json'
INFILE_LANDTAGE = 'db_dump/data/factions/factions-landtage-rawqueryresults.json'
OUTFILE = 'db_dump/data/factions/factions-formatted.json'


def reformat(obj):
    flat = {key : value['value'] for (key, value) in obj.items()}
    id = flat.pop('faction').split('/')[-1]
    label = flat.pop('factionLabel')
    new = {
        'type': 'faction', 
        'id': id, 
        'label': label,
        'socialMediaIDs': helpers.group_socials(flat),
        **flat
    }
    return new

# map over the entries and reformat each of them (reformatting means changing property names or grouping properties)
with open(INFILE_BUNDESTAG) as infile_bundestag:
    with open(INFILE_LANDTAGE) as infile_landtage:
        data_bundestag = json.load(infile_bundestag)
        data_landtage = json.load(infile_landtage)
        entries_bundestag = [reformat(entry) for entry in data_bundestag['results']['bindings']]
        entries_landtage = [reformat(entry) for entry in data_landtage['results']['bindings']]
        entries = entries_bundestag + entries_landtage
        helpers.check_for_dups(entries)
        with open(OUTFILE, 'w', encoding='utf8') as outfile:
            json.dump(entries, outfile, ensure_ascii=False)

