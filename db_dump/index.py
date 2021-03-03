import wikidata.client as wikidata_client
from wikidata.queries import get_all_members_of_parliament


query = get_all_members_of_parliament
results = wikidata_client.get(query)

print(results)