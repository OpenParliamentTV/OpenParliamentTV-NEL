
import wikidata_client;
from wikidata_query_constructor import get_members_of_parliament;

query = get_members_of_parliament(name="merkel", parliament="DE", date="1948-01-01")

results = wikidata_client.get(query)
print(results)

for result in results["results"]["bindings"]:
    print(result)
