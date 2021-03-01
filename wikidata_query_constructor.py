
from wikidata_id_mappings import INSTANCE_OF, HUMAN, DATE_OF_BIRTH, DATE_OF_DEATH, POSITION_HELD, MEMBER_OF_PARLIAMENT
from wikidata_helpers import convert_to_property_statement as cps

def get_members_of_parliament(name="", parliament='DE', date=None):
    query_string_1 = """SELECT DISTINCT ?mdb WHERE {{
        ?mdb {instance_of} {human}.
        ?mdb {position_held} ?humansWithPositionHeld.
        ?humansWithPositionHeld {position_held_ps} {member_parliament_de}.
        ?mdb rdfs:label ?mdbString.
        FILTER(CONTAINS(LCASE(?mdbString), "{name}"@de)).""".format(instance_of = INSTANCE_OF, human = HUMAN, position_held = POSITION_HELD, position_held_ps = cps(POSITION_HELD), member_parliament_de=MEMBER_OF_PARLIAMENT[parliament], name = name)
    
    query_string_2 = """
        ?mdb {date_of_birth} ?birth.
        FILTER(?birth < "{date}"^^xsd:dateTime).
        OPTIONAL {{ ?mdb {date_of_death} ?death. }}
        FILTER(!BOUND(?death) || ?death > "{date}"^^xsd:dateTime).""".format(date_of_birth=DATE_OF_BIRTH, date=date, date_of_death=DATE_OF_DEATH)
    
    query_string_3 = """
        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],de". }
        }
        LIMIT 16"""
    query = ''.join([query_string_1, (query_string_2 if date else ''), query_string_3])
    print(query)
    return query

