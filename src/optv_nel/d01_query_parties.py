from pathlib import Path
import json
import optv_nel.wikidata.client as wikidata_client
from optv_nel.wikidata.queries import get_all_parties_of_germany

OUTPATH = Path("data/01_raw/parties")
OUTFILE = Path('parties.json')
OUTPATH.mkdir(parents=True, exist_ok=True)

query = get_all_parties_of_germany()
results = wikidata_client.get(query)
print(results)
with open(OUTPATH / OUTFILE, 'w', encoding='utf8') as outfile:
    json.dump(results, outfile, ensure_ascii=False)