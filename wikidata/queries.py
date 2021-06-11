from wikidata.mappings import MAPPINGS as WIKIDATA_MAPPINGS
from wikidata.helpers import convert_to_property_statement as cps
from wikidata.helpers import convert_to_qualifier_statement as cpq


def get_all_parties_of_germany():
    query_string = """
    SELECT DISTINCT ?ppg ?ppgLabel ?labelAlternative ?abstract ?thumbnailURI ?websiteURI ?instagram ?facebook ?twitter WHERE {{
        ?ppg {INSTANCE_OF} {POLITICAL_PARTY_IN_GERMANY}.
        OPTIONAL {{?ppg {SHORT_NAME} ?labelAlternative. FILTER(lang(?labelAlternative) = "de").}}
        OPTIONAL {{?ppg schema:description ?abstract. FILTER(lang(?abstract) = "de").}}
        OPTIONAL {{ ?ppg {DISSOLVED_DATE} ?endDate. }}
        OPTIONAL {{ ?ppg {OFFICIAL_WEBSITE} ?websiteURI. }}
        OPTIONAL {{ ?ppg {INSTAGRAM_USERNAME} ?instagram. }}
        OPTIONAL {{ ?ppg {FACEBOOK_USERNAME} ?facebook. }}
        OPTIONAL {{ ?ppg {TWITTER_USERNAME} ?twitter. }}
        OPTIONAL {{
            ?ppg {LOGO_IMG} ?image_.
            BIND(REPLACE(wikibase:decodeUri(STR(?image_)), "http://commons.wikimedia.org/wiki/Special:FilePath/", "") AS ?imageFileName_)
            BIND(REPLACE(?imageFileName_, " ", "_") AS ?imageFileNameSafe_)
            BIND(MD5(?imageFileNameSafe_) AS ?imageFileNameHash_)
            BIND(CONCAT("https://upload.wikimedia.org/wikipedia/commons/thumb/", SUBSTR(?imageFileNameHash_, 1 , 1 ), "/", SUBSTR(?imageFileNameHash_, 1 , 2 ), "/", ?imageFileNameSafe_, "/300px-", ?imageFileNameSafe_) AS ?thumbnailURI)
        }}
        FILTER (!BOUND(?endDate) || '1949-01-01'^^xsd:dateTime <= ?endDate)
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "de". }}
    }}
    """.format(**WIKIDATA_MAPPINGS)
    print(query_string)
    return query_string


def get_all_members_of_parliament(parliament='DE'):    
    query_string = """
    SELECT DISTINCT ?mdb ?mdbLabel ?faction ?abstract ?dateOfBirth ?dateOfDeath ?abgeordnetenwatchID ?thumbnailURI ?party ?gender ?websiteURI ?instagram ?facebook ?twitter WITH {{
        SELECT ?mdb ?humansWithPositionHeld WHERE {{
            ?mdb {INSTANCE_OF} {HUMAN}.
            ?mdb {POSITION_HELD} ?humansWithPositionHeld.
            ?humansWithPositionHeld {position_held_ps} {member_of_parliament}.
        }} }} AS %i
    WHERE {{
        INCLUDE %i
        OPTIONAL {{ ?humansWithPositionHeld {parliamentary_group_pq} ?faction. }}
        OPTIONAL {{ ?mdb {DATE_OF_BIRTH} ?dateOfBirth. }}
        OPTIONAL {{ ?mdb {DATE_OF_DEATH} ?dateOfDeath. }}
        OPTIONAL {{ ?mdb {ABGEORDNETENWATCH_ID} ?abgeordnetenwatchID. }}
        OPTIONAL {{
            ?mdb wdt:P18 ?image_.
            BIND(REPLACE(wikibase:decodeUri(STR(?image_)), "http://commons.wikimedia.org/wiki/Special:FilePath/", "") AS ?imageFileName_)
            BIND(REPLACE(?imageFileName_, " ", "_") AS ?imageFileNameSafe_)
            BIND(MD5(?imageFileNameSafe_) AS ?imageFileNameHash_)
            BIND(CONCAT("https://upload.wikimedia.org/wikipedia/commons/thumb/", SUBSTR(?imageFileNameHash_, 1 , 1 ), "/", SUBSTR(?imageFileNameHash_, 1 , 2 ), "/", ?imageFileNameSafe_, "/300px-", ?imageFileNameSafe_) AS ?thumbnailURI)
        }}
        OPTIONAL {{ ?mdb {MEMBER_OF_POLITICAL_PARTY} ?party. OPTIONAL {{?party {DISSOLVED_DATE} ?partyEndDate_.}} }}
        FILTER('1949-01-01'^^xsd:dateTime <= ?partyEndDate_ || !BOUND(?partyEndDate_)).
        OPTIONAL {{
            ?mdb {SEX_OR_GENDER} ?gender_. ?gender_ rdfs:label ?genderLabel_. 
            FILTER(lang(?genderLabel_) = "en"). 
        }}
        BIND(IF(BOUND(?genderLabel_ ), ?genderLabel_, "unknown") AS ?gender).
        OPTIONAL {{ ?mdb {OFFICIAL_WEBSITE} ?websiteURI. }}
        OPTIONAL {{ ?mdb {INSTAGRAM_USERNAME} ?instagram. }}
        OPTIONAL {{ ?mdb {FACEBOOK_USERNAME} ?facebook. }}
        OPTIONAL {{ ?mdb {TWITTER_USERNAME} ?twitter. }}
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "de". ?mdb rdfs:label ?mdbLabel. ?mdb schema:description ?abstract. }}
        }}
        """.format(**WIKIDATA_MAPPINGS, position_held_ps = cps(WIKIDATA_MAPPINGS['POSITION_HELD']), parliamentary_group_pq = cpq(WIKIDATA_MAPPINGS['PARLIAMENTARY_GROUP']), member_of_parliament = WIKIDATA_MAPPINGS['MEMBER_OF_PARLIAMENT'][parliament])
    print(query_string)
    return query_string


# Early solution without the query optimisation with INCLUDE statement
# The query for all members of parliament would most probably time out  :-/
# Workaround is to filter the members by date of birth, and get the results in multiple batches
def get_all_members_of_parliament_filtered_by_birth(parliament='DE', min_birth='1800-01-01', max_birth='2030-01-01'):    
    query_string = """
    SELECT DISTINCT ?mdb ?mdbLabel ?faction ?abstract ?dateOfBirth ?dateOfDeath ?abgeordnetenwatchID ?thumbnailURI ?party ?gender ?websiteURI ?instagram ?facebook ?twitter WHERE {{
        ?mdb {INSTANCE_OF} {HUMAN}.
        ?mdb {POSITION_HELD} ?humansWithPositionHeld.
        ?humansWithPositionHeld {position_held_ps} {member_of_parliament}.
        OPTIONAL {{ ?humansWithPositionHeld {parliamentary_group_pq} ?faction. }}
        ?mdb rdfs:label ?mdbString.
        OPTIONAL {{ ?mdb schema:description ?abstract. FILTER(lang(?abstract) = "de"). }}
        OPTIONAL {{ ?mdb {DATE_OF_BIRTH} ?dateOfBirth. }}
        OPTIONAL {{ ?mdb {DATE_OF_DEATH} ?dateOfDeath. }}
        OPTIONAL {{ ?mdb {ABGEORDNETENWATCH_ID} ?abgeordnetenwatchID. }}
        OPTIONAL {{
            ?mdb wdt:P18 ?image_.
            BIND(REPLACE(wikibase:decodeUri(STR(?image_)), "http://commons.wikimedia.org/wiki/Special:FilePath/", "") AS ?imageFileName_)
            BIND(REPLACE(?imageFileName_, " ", "_") AS ?imageFileNameSafe_)
            BIND(MD5(?imageFileNameSafe_) AS ?imageFileNameHash_)
            BIND(CONCAT("https://upload.wikimedia.org/wikipedia/commons/thumb/", SUBSTR(?imageFileNameHash_, 1 , 1 ), "/", SUBSTR(?imageFileNameHash_, 1 , 2 ), "/", ?imageFileNameSafe_, "/300px-", ?imageFileNameSafe_) AS ?thumbnailURI)
        }}
        OPTIONAL {{ ?mdb {MEMBER_OF_POLITICAL_PARTY} ?party. }}
        OPTIONAL {{
            ?mdb {SEX_OR_GENDER} ?gender_. ?gender_ rdfs:label ?genderLabel_. 
            FILTER(lang(?genderLabel_) = "en"). 
        }}
        BIND(IF(BOUND(?genderLabel_ ), ?genderLabel_, "unknown") AS ?gender).
        OPTIONAL {{ ?mdb {OFFICIAL_WEBSITE} ?websiteURI. }}
        OPTIONAL {{ ?mdb {INSTAGRAM_USERNAME} ?instagram. }}
        OPTIONAL {{ ?mdb {FACEBOOK_USERNAME} ?facebook. }}
        OPTIONAL {{ ?mdb {TWITTER_USERNAME} ?twitter. }}
        FILTER('{min_birth}'^^xsd:dateTime <= ?dateOfBirth && ?dateOfBirth < '{max_birth}'^^xsd:dateTime).
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],de". }}
        }}
        """.format(**WIKIDATA_MAPPINGS, position_held_ps = cps(WIKIDATA_MAPPINGS['POSITION_HELD']), parliamentary_group_pq = cpq(WIKIDATA_MAPPINGS['PARLIAMENTARY_GROUP']), member_of_parliament = WIKIDATA_MAPPINGS['MEMBER_OF_PARLIAMENT'][parliament], min_birth = min_birth, max_birth = max_birth)
    print(query_string)
    return query_string

