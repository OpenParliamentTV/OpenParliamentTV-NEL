
from wikidata_id_mappings import INSTANCE_OF, HUMAN, DATE_OF_BIRTH, DATE_OF_DEATH, POSITION_HELD, MEMBER_OF_PARLIAMENT
from wikidata_helpers import convert_to_property_statement as cps

def get_members_of_parliament(name="", parliament='DE', date=None):
    query_string = """SELECT DISTINCT ?mdb WHERE {{
        ?mdb {instance_of} {human}.
        ?mdb {position_held} ?humansWithPositionHeld.
        ?humansWithPositionHeld {position_held_ps} {member_parliament_de}.
        ?mdb rdfs:label ?mdbString.
        ?mdb {date_of_birth} ?birth.
        FILTER(CONTAINS(LCASE(?mdbString), "{name}"@de)).
        FILTER(?birth < "{date}"^^xsd:dateTime).
        OPTIONAL {{ ?mdb {date_of_death} ?death. }}
        FILTER(!BOUND(?death) || ?death > "{date}"^^xsd:dateTime).
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],de". }}
        }}
        LIMIT 16""".format(instance_of = INSTANCE_OF, human = HUMAN, position_held = POSITION_HELD, position_held_ps = cps(POSITION_HELD), member_parliament_de=MEMBER_OF_PARLIAMENT[parliament], date_of_birth=DATE_OF_BIRTH, date_of_death=DATE_OF_DEATH, name = name, date=date)
    print(query_string)
    return query_string

