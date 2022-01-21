import json
PARTY_MAPPING_FILE = 'data/04_mappings/parties/abgeordnetenwatch_to_wikidata.json'

#TODO: This could be improved by strictly checking IDs instead of fuzzy stringmatching..
def convert_to_wikidata_faction_id(aw_faction_object, parliament):
    faction_label = aw_faction_object.get('fraction', {}).get('label')
    if parliament == 'DE':
        if 'fraktionslos' in faction_label:
            return "Q4316268" #Non-attached deputy
        if 'FDP' in faction_label:
            return "Q1387991" #FDP Bundestag faction
        if 'SPD' in faction_label:
            return "Q2207512" #SPD Bundestag faction
        if 'CDU/CSU' in faction_label:
            return "Q1023134" #CDU/CSU Bundestag faction
        if 'DIE LINKE' in faction_label:
            return  "Q1826856" #Bundestag faction Die Linke
        if 'AfD' in faction_label:
            return "Q42575708" #AfD Bundestag faction
        if 'DIE GRÜNEN' in faction_label:
            return "Q1007353" #Green Party faction 
    elif parliament == 'DE-BB':
        if 'fraktionslos' in faction_label:
            return "Q4316268" #Non-attached deputy
        if 'Freie Wähler' in faction_label:
            return "Q108583293" #BVB/Freie Wähler faction Landtag BB
        if 'SPD' in faction_label:
            return "Q108583167" #SPD faction Landtag BB
        if 'CDU' in faction_label:
            return "Q108583055" #CDU faction Landtag BB
        if 'DIE LINKE' in faction_label:
            return  "Q108583412" #Die Linke faction Landtag BB
        if 'AfD' in faction_label:
            return "Q108583380" #AfD faction Landtag BB
        if 'Die Grünen' in faction_label:
            return "Q108583221" #Green Party faction Landtag BB
    return faction_label


def convert_to_wikidata_party_id(aw_party_object):
    with open(PARTY_MAPPING_FILE) as party_mapping_file:
        party_mapping = json.load(party_mapping_file)
        aw_party_id = str(aw_party_object.get('id'))
        if aw_party_id not in party_mapping:
            return aw_party_object.get('label')
        return party_mapping[aw_party_id]