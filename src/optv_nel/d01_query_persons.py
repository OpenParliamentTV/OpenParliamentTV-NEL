import json
import optv_nel.wikidata.client as wikidata_client
from optv_nel.wikidata.queries import get_all_members_of_parliament, get_all_potential_other_speakers_in_bundestag

PARLIAMENTS = ["DE", "DE-BB"] # German Bundestag, Landtag Brandenburg

for PARLIAMENT in PARLIAMENTS:
    OUTFILE = 'data/01_raw/persons/' + PARLIAMENT + '.json'
    query = get_all_members_of_parliament(parliament=PARLIAMENT)
    results = wikidata_client.get(query)
    with open(OUTFILE, 'w', encoding='utf8') as outfile:
        json.dump(results, outfile, ensure_ascii=False)

#Additional: Other speakers for German Bundestag
OUTFILE = 'data/01_raw/persons/DE_extra.json'
query = get_all_potential_other_speakers_in_bundestag()
results = wikidata_client.get(query)
with open(OUTFILE, 'w', encoding='utf8') as outfile:
    json.dump(results, outfile, ensure_ascii=False)