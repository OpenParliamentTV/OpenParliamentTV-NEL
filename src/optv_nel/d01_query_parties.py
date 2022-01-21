OUTFILE = 'data/01_raw/parties/rawqueryresults.json'

import json
import optv_nel.wikidata.client as wikidata_client
from optv_nel.wikidata.queries import get_all_parties_of_germany

query = get_all_parties_of_germany()
results = wikidata_client.get(query)
print(results)
with open(OUTFILE, 'w', encoding='utf8') as outfile:
    json.dump(results, outfile, ensure_ascii=False)