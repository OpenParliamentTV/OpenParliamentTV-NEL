import wikidata.wikidata_client
from wikidata.wikidata_query_constructor import get_all_members_of_parliament


query = get_all_members_of_parliament
results = wikidata_client.get(query)

print(results)