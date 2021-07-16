import json

INFILE = './db_dump/data/mdbs/mdbs-final.json'

#group by keyname...
with open(INFILE) as infile:
    data = json.load(infile)
    print("all entries", len(data))
    reduced = {}
    for entry in data:
        key = entry.get('AwFactionID', None)
        if key is not None:
            if key not in reduced:
                reduced[key] = []
            reduced[key].append(entry['id'])
    #print(reduced)

#group by keyname...
with open(INFILE) as infile:
    data = json.load(infile)
    print("all entries", len(data))
    needles = [needle['id'] for needle in data if needle.get('factionID') is not None and needle.get('AwFactionID') is not None and needle['factionID'] != needle['AwFactionID']] 
    for entry in data:
        key = entry.get('AwFactionID', None)
        if key is not None:
            if key not in reduced:
                reduced[key] = []
            reduced[key].append(entry['id'])
    print(needles)