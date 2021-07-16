#Bundestag Fraktionen...
#TODO: This could be improved by strictly checking IDs instead of fuzzy stringmatching..
def convert_to_wikidata_faction_id(label_text):
    if 'fraktionslos' in label_text:
        return "Q4316268" #Non-attached deputy
    if 'FDP' in label_text:
        return "Q1387991" #FDP Bundestag fraction
    if 'SPD' in label_text:
        return "Q2207512" #SPD Bundestag fraction
    if 'CDU/CSU' in label_text:
        return "Q1023134" #CDU/CSU Bundestag fraction
    if 'DIE LINKE' in label_text:
        return  "Q1826856" #Bundestag fraction Die Linke
    if 'AfD' in label_text:
        return "Q42575708" #AfD Bundestag fraction
    if 'DIE GRÜNEN' in label_text:
        return "Q1007353" #Green Party fraction 
    return label_text