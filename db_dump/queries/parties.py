import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(rootdir)

OUTFILE = 'db_dump/data/parties/parties-rawqueryresults.json'

import json
import wikidata.client as wikidata_client
from wikidata.queries import get_all_parties_of_germany

query = get_all_parties_of_germany()
results = wikidata_client.get(query)
print(results)
with open(OUTFILE, 'w') as outfile:
    json.dump(results, outfile)
