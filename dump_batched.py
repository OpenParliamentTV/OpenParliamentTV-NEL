import sys
import json
import wikidata.client as wikidata_client
from wikidata.queries import get_all_members_of_parliament

BATCH_OFFSET = 0
try:
    BATCH_OFFSET = int(sys.argv[1])
except:
    pass

batches = [
    {'max_birth': '1900-01-01'},
    {'min_birth': '1900-01-01', 'max_birth': '1910-01-01'},
    {'min_birth': '1910-01-01', 'max_birth': '1920-01-01'},
    {'min_birth': '1920-01-01', 'max_birth': '1930-01-01'},
    {'min_birth': '1930-01-01', 'max_birth': '1940-01-01'},
    {'min_birth': '1940-01-01', 'max_birth': '1950-01-01'},
    {'min_birth': '1950-01-01', 'max_birth': '1960-01-01'},
    {'min_birth': '1960-01-01', 'max_birth': '1970-01-01'},
    {'min_birth': '1970-01-01', 'max_birth': '1975-01-01'},
    {'min_birth': '1975-01-01', 'max_birth': '1980-01-01'},
    {'min_birth': '1980-01-01'},
]

for batch in batches[BATCH_OFFSET:]:
    query = get_all_members_of_parliament(parliament="DE", **batch)
    results = wikidata_client.get(query)
    file = 'mdb_' + batch.get('min_birth', 'before') + '__' + batch.get('max_birth', 'after') + '.json'
    with open(file, 'w') as outfile:
        json.dump(results, outfile)
