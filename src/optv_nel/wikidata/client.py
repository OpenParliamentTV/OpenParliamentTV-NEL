# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import SPARQLWrapper, JSON

ENDPOINT_URL = "https://query.wikidata.org/sparql"

def get(query):
    user_agent = "OpenParliamentTV/0.1 (https://openparliament.tv; joscha.jaeger@openparliament.tv)"
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(ENDPOINT_URL, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()
