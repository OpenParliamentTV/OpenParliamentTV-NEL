from wikidata.mappings import MAPPINGS as WIKIDATA_MAPPINGS
from wikidata.helpers import convert_to_property_statement as cps

# The query for all members of parliament will most probably time out  :-/
# Workaround is to filter the members by date of birth, and get the results in multiple batches

def get_all_members_of_parliament(parliament='DE', min_birth='1800-01-01', max_birth='2030-01-01'):    
    query_string = """SELECT DISTINCT ?mdb ?mdbLabel ?familyName ?givenName ?dateOfBirth ?dateOfDeath ?degree ?abgeordnetenwatchID ?thumbnailURI ?party ?gender ?websiteURI ?insta WHERE {{
        ?mdb {INSTANCE_OF} {HUMAN}.
        ?mdb {POSITION_HELD} ?humansWithPositionHeld.
        ?humansWithPositionHeld {position_held_ps} {member_of_parliament}.
        ?mdb rdfs:label ?mdbString.
        OPTIONAL {{?mdb {FAMILY_NAME}/{NATIVE_LABEL} ?familyName. }}
        OPTIONAL {{?mdb {GIVEN_NAME}/{NATIVE_LABEL} ?givenName. }}
        OPTIONAL {{?mdb {DATE_OF_BIRTH} ?dateOfBirth. }}
        OPTIONAL {{?mdb {DATE_OF_DEATH} ?dateOfDeath. }}
        OPTIONAL {{?mdb {ACADEMIC_DEGREE} ?degree. }}
        OPTIONAL {{?mdb {ABGEORDNETENWATCH_ID} ?abgeordnetenwatchID. }}
        OPTIONAL {{?mdb {IMAGE} ?thumbnailURI. }}
        OPTIONAL {{?mdb {MEMBER_OF_POLITICAL_PARTY}/{SHORT_NAME} ?party. }}
        OPTIONAL {{?mdb {SEX_OR_GENDER} ?genderEntity. }}
        BIND(IF(?genderEntity = {GENDER_MALE}, "male", "female") AS ?gender).
        OPTIONAL {{?mdb {OFFICIAL_WEBSITE} ?websiteURI. }}
        OPTIONAL {{?mdb {INSTAGRAM_USERNAME} ?insta. }}
        FILTER('{min_birth}'^^xsd:dateTime <= ?dateOfBirth && ?dateOfBirth < '{max_birth}'^^xsd:dateTime).
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],de". }}
        }}
        """.format(**WIKIDATA_MAPPINGS, position_held_ps = cps(WIKIDATA_MAPPINGS['POSITION_HELD']), member_of_parliament = WIKIDATA_MAPPINGS['MEMBER_OF_PARLIAMENT'][parliament], min_birth = min_birth, max_birth = max_birth)
    print(query_string)
    return query_string




def get_members_of_parliament(name="", parliament='DE', date=None):
    query_string_1 = """SELECT DISTINCT ?mdb ?mdbLabel ?familyName ?givenName ?dateOfBirth ?dateOfDeath ?degree ?abgeordnetenwatchID WHERE {{
        ?mdb {INSTANCE_OF} {HUMAN}.
        ?mdb {POSITION_HELD} ?humansWithPositionHeld.
        ?humansWithPositionHeld {position_held_ps} {member_of_parliament}.
        ?mdb rdfs:label ?mdbString.
        ?mdb {FAMILY_NAME}/{NATIVE_LABEL} ?familyName.
        ?mdb {GIVEN_NAME}/{NATIVE_LABEL} ?givenName.
        ?mdb {DATE_OF_BIRTH} ?dateOfBirth.
        OPTIONAL {{ ?mdb {DATE_OF_DEATH} ?dateOfDeath. }}
        OPTIONAL {{ ?mdb {ACADEMIC_DEGREE} ?degree. }}
        OPTIONAL {{ ?mdb {ABGEORDNETENWATCH_ID} ?abgeordnetenwatchID. }}
        FILTER(CONTAINS(LCASE(?mdbString), "{name}"@de))."""\
            .format(**WIKIDATA_MAPPINGS, name = name, position_held_ps = cps(WIKIDATA_MAPPINGS['POSITION_HELD']), \
                member_of_parliament = WIKIDATA_MAPPINGS['MEMBER_OF_PARLIAMENT'][parliament])
    
    query_string_2 = """
        FILTER(?dateOfBirth < "{date}"^^xsd:dateTime).
        FILTER(!BOUND(?dateOfDeath) || ?dateOfDeath > "{date}"^^xsd:dateTime).""".format(**WIKIDATA_MAPPINGS, date = date)
    
    query_string_3 = """
        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],de". }
        }
        LIMIT 16"""
    query = ''.join([query_string_1, (query_string_2 if date else ''), query_string_3])
    print(query)
    return query

