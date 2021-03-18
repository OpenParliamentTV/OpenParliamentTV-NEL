import json

with open('./db_dump/mdb-with-dups.json') as infile:
    data = json.load(infile)
    unique = { each['mdb'] : each for each in data }.values()
    print(len(unique))
    with open('./db_dump/mdb.json', 'w') as outfile:
        json.dump([u for u in unique], outfile)


