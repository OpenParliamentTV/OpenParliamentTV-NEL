#go through wikidata parties dump in db_dump/data/parties/parties-final.json
#for each party check the label in the abgeordnetenwatch dump (important: matching has to be case insensitive!)
#generate a new python file with the mappings...


import json
import os
import sys

#add project root to path so I can import a module from the wikidata folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))

PARTY_DUMP_WIKIDATA = './db_dump/data/parties/parties-final.json'
PARTY_DUMP_ABGEORDNETENWATCH = './abgeordnetenwatch/dump/parties.json'
OUTFILE = './abgeordnetenwatch/party-mapping.json'

#go through wikidata parties dump in db_dump/data/parties/parties-final.json
with open(PARTY_DUMP_WIKIDATA) as parties_wikidata_file:
    with open(PARTY_DUMP_ABGEORDNETENWATCH) as parties_abgeordnetenwatch_file:
        parties_wikidata = json.load(parties_wikidata_file)
        parties_abgeordnetenwatch = json.load(parties_abgeordnetenwatch_file).get('data')
        mapping = {}
        for party_wd in parties_wikidata:
            party_label_wd = party_wd.get('label', '')
            party_label_alternative_wd = party_wd.get('labelAlternative', '')
            try:
                aw_match = next(p_aw for p_aw in parties_abgeordnetenwatch if p_aw.get('label', '').lower() == party_label_wd.lower() or p_aw.get('label', '').lower() in party_label_alternative_wd)
                mapping[aw_match['id']] = party_wd['id']
            except StopIteration:
                print(party_label_wd)
        with open(OUTFILE, 'w', encoding='utf8') as outfile:
            pass
            json.dump(mapping, outfile, ensure_ascii=False)