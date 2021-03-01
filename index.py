
import wikidata_client;
from wikidata_query_contructor import get_members_of_parliament;

query = get_members_of_parliament_by_name(name="merkel", parliament="DE")

results = wikidata_client.get(query)
print(results)

for result in results["results"]["bindings"]:
    print(result)
