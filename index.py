
import wikidata_client;
from wikidata_query_contructor import get_query_string;

query = get_query_string(needle="merkel")

results = wikidata_client.get(query)
print(results)

for result in results["results"]["bindings"]:
    print(result)
