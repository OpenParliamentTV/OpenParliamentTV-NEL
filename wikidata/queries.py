from wikidata.mappings import MAPPINGS as WIKIDATA_MAPPINGS
from wikidata.helpers import convert_to_property_statement as cps

def get_all_members_of_parliament(parliament='DE'):    
    query_string = """SELECT DISTINCT ?mdb ?mdbLabel ?familyName ?givenName ?dateOfBirth ?dateOfDeath ?academicDegree ?abgeordnetenwatchID WHERE {{
        ?mdb {INSTANCE_OF} {HUMAN}.
        ?mdb {POSITION_HELD} ?humansWithPositionHeld.
        ?humansWithPositionHeld {position_held_ps} {member_of_parliament}.
        ?mdb rdfs:label ?mdbString.
        ?mdb {FAMILY_NAME} ?familyName.
        ?mdb {GIVEN_NAME} ?givenName.
        ?mdb {DATE_OF_BIRTH} ?dateOfBirth.
        OPTIONAL {{?mdb {DATE_OF_DEATH} ?dateOfDeath. }}
        OPTIONAL {{?mdb {ACADEMIC_DEGREE} ?degree. }}
        OPTIONAL {{?mdb {ABGEORDNETENWATCH_ID} ?abgeordnetenwatchID. }}
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],de". }}
        }}
        LIMIT 10
        """.format(**WIKIDATA_MAPPINGS, position_held_ps = cps(WIKIDATA_MAPPINGS['POSITION_HELD']), member_of_parliament = WIKIDATA_MAPPINGS['MEMBER_OF_PARLIAMENT'][parliament])
    print(query_string)
    return query_string


def get_members_of_parliament(name="", parliament='DE', date=None):
    query_string_1 = """SELECT DISTINCT ?mdb WHERE {{
        ?mdb {INSTANCE_OF} {HUMAN}.
        ?mdb {POSITION_HELD} ?humansWithPositionHeld.
        ?humansWithPositionHeld {position_held_ps} {member_of_parliament}.
        ?mdb rdfs:label ?mdbString.
        FILTER(CONTAINS(LCASE(?mdbString), "{name}"@de)).""".format(**WIKIDATA_MAPPINGS, name = name, position_held_ps = cps(WIKIDATA_MAPPINGS['POSITION_HELD']), member_of_parliament = WIKIDATA_MAPPINGS['MEMBER_OF_PARLIAMENT'][parliament])
    
    query_string_2 = """
        ?mdb {DATE_OF_BIRTH} ?birth.
        FILTER(?birth < "{date}"^^xsd:dateTime).
        OPTIONAL {{ ?mdb {DATE_OF_DEATH} ?death. }}
        FILTER(!BOUND(?death) || ?death > "{date}"^^xsd:dateTime).""".format(**WIKIDATA_MAPPINGS, date = date)
    
    query_string_3 = """
        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],de". }
        }
        LIMIT 16"""
    query = ''.join([query_string_1, (query_string_2 if date else ''), query_string_3])
    print(query)
    return query

