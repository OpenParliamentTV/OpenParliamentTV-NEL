import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
rootdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(rootdir)

import json
import wikidata.client as wikidata_client
from wikidata.queries import get_all_members_of_parliament

PARLIAMENTS = ["DE", "DE-BB"] # German Bundestag, Landtag Brandenburg

for PARLIAMENT in PARLIAMENTS:
    OUTFILE = 'db_dump/data/mdbs/mdbs-rawqueryresults_' + PARLIAMENT + '.json'
    query = get_all_members_of_parliament(parliament=PARLIAMENT)
    results = wikidata_client.get(query)
    with open(OUTFILE, 'w', encoding='utf8') as outfile:
        json.dump(results, outfile, ensure_ascii=False)