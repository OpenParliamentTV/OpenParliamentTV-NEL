
import wikidata.client as wikidata_client;
from wikidata.queries import get_members_of_parliament;

query = get_members_of_parliament(name="merkel", parliament="DE", date="2020-01-01")

results = wikidata_client.get(query)
print(results)

for result in results["results"]["bindings"]:
    print(result)
