OUTFILE_BUNDESTAG = 'db_dump/data/factions/rawqueryresults-bundestag.json'
OUTFILE_LANDTAGE = 'db_dump/data/factions/rawqueryresults-landtage.json'

import json
import optv_nel.wikidata.client as wikidata_client
from optv_nel.wikidata.queries import get_all_bundestag_factions_of_germany
from optv_nel.wikidata.queries import get_all_landtag_factions_of_germany

query_bundestag = get_all_bundestag_factions_of_germany()
query_landtage = get_all_landtag_factions_of_germany()

results_bundestag = wikidata_client.get(query_bundestag)
results_landtage = wikidata_client.get(query_landtage)

with open(OUTFILE_BUNDESTAG, 'w', encoding='utf8') as outfile:
    json.dump(results_bundestag, outfile, ensure_ascii=False)

with open(OUTFILE_LANDTAGE, 'w', encoding='utf8') as outfile:
    json.dump(results_landtage, outfile, ensure_ascii=False)

