
from wikidata_id_mappings import INSTANCE_OF, HUMAN, POSITION_HELD, MEMBER_OF_PARLIAMENT
from wikidata_helpers import convert_to_property_statement as cps

def get_query_string(needle=""):
    query_string = """SELECT DISTINCT ?mdb WHERE {{
        ?mdb {instance_of} {human}.
        ?mdb {position_held} ?humansWithPositionHeld.
        ?humansWithPositionHeld {position_held_ps} {memberParliamentDe}.
        ?mdb rdfs:label ?mdbString.
        FILTER(CONTAINS(LCASE(?mdbString), "{needle}"@de))
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],de". }}
        }}
        LIMIT 16""".format(instance_of = INSTANCE_OF, human = HUMAN, position_held = POSITION_HELD, position_held_ps = cps(POSITION_HELD), memberParliamentDe=MEMBER_OF_PARLIAMENT['DE'], needle = needle)
    print(query_string)
    return query_string

