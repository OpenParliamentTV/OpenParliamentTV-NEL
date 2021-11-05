import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(rootdir)

import json
import wikidata.client as wikidata_client
from wikidata.queries import get_all_potential_other_speakers_in_bundestag

OUTFILE = 'db_dump/data/other-speakers/other-speakers-rawqueryresults.json'

query_DE = get_all_potential_other_speakers_in_bundestag()

results_DE = wikidata_client.get(query_DE)

with open(OUTFILE, 'w', encoding='utf8') as outfile:
    json.dump(results_DE, outfile, ensure_ascii=False)