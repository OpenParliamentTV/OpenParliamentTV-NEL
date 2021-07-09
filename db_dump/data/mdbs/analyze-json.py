import json

INFILE = './db_dump/data/mdbs/all-mdbs-with-abgwatchid.json'

with open(INFILE) as infile:
    data = json.load(infile)
    print("all entries", len(data))
    reduced = {}
    for entry in data:
        key = entry['mdb']
        if key not in reduced:
            reduced[key] = []
        reduced[key].append(entry)
    print([e for e in reduced.values() if len(e)>1])
    print(len(reduced.keys()))
