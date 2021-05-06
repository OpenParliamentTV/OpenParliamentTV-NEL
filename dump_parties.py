import json
import wikidata.client as wikidata_client
from wikidata.queries import get_all_parties_of_germany

query = get_all_parties_of_germany()
results = wikidata_client.get(query)
print(results)
with open('parties.json', 'w') as outfile:
    json.dump(results, outfile)
