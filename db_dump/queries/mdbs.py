import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(rootdir)

import json
import wikidata.client as wikidata_client
from wikidata.queries import get_all_members_of_parliament

# German Bundestag

OUTFILE_DE = 'db_dump/data/mdbs/mdbs-rawqueryresults_DE.json'

query_DE = get_all_members_of_parliament(parliament="DE")

results_DE = wikidata_client.get(query_DE)
#print(results_DE)

with open(OUTFILE_DE, 'w', encoding='utf8') as outfile_DE:
    json.dump(results_DE, outfile_DE, ensure_ascii=False)

# Landtag Brandenburg

OUTFILE_DE_BB = 'db_dump/data/mdbs/mdbs-rawqueryresults_DE-BB.json'

query_DE_BB = get_all_members_of_parliament(parliament="DE-BB")

results_DE_BB = wikidata_client.get(query_DE_BB)

with open(OUTFILE_DE_BB, 'w', encoding='utf8') as outfile_DE_BB:
    json.dump(results_DE_BB, outfile_DE_BB, ensure_ascii=False)
