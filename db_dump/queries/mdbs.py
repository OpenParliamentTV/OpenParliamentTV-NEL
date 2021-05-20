import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(rootdir)

import json
import wikidata.client as wikidata_client
from wikidata.queries import get_all_members_of_parliament


query = get_all_members_of_parliament(parliament="DE")
results = wikidata_client.get(query)
print(results)
with open('mdb.json', 'w') as outfile:
    json.dump(results, outfile)
