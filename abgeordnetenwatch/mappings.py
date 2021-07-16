#Bundestag Fraktionen...
#TODO: This could be improved by strictly checking IDs instead of fuzzy stringmatching..
def convert_to_wikidata_faction_id(aw_faction_object):
    faction_label = aw_faction_object.get('fraction', {}).get('label')
    if 'fraktionslos' in faction_label:
        return "Q4316268" #Non-attached deputy
    if 'FDP' in faction_label:
        return "Q1387991" #FDP Bundestag fraction
    if 'SPD' in faction_label:
        return "Q2207512" #SPD Bundestag fraction
    if 'CDU/CSU' in faction_label:
        return "Q1023134" #CDU/CSU Bundestag fraction
    if 'DIE LINKE' in faction_label:
        return  "Q1826856" #Bundestag fraction Die Linke
    if 'AfD' in faction_label:
        return "Q42575708" #AfD Bundestag fraction
    if 'DIE GRÜNEN' in faction_label:
        return "Q1007353" #Green Party fraction 
    return faction_label


def convert_to_wikidata_party_id(aw_party_object):
    aw_party_id = aw_party_object.get('id')
    print(aw_party_id)
    if aw_party_id == 1:
        return "QSPD"
    if aw_party_id == 2:
        return 'QCDU'
    if aw_party_id == 3:
        return 'QCSU'
    if aw_party_id == 4:
        return 'QFDP'
    if aw_party_id == 5:
        return 'QGRÜ'
    if aw_party_id == 6:
        return 'PIRATEN'
    
    return aw_party_object.get('label')
