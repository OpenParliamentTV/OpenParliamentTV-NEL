import sys
import os
import json

#FILE = './db_dump/mdb-with-dups.json'
INFILE = sys.argv[1]
OUTFILE = os.path.splitext(INFILE)[0] + '_no_dups.json'

try:
    OUTFILE = sys.argv[2]
except:
    print("Output file saved as: ", OUTFILE)

with open(INFILE) as infile:
    data = json.load(infile)
    unique = { each['mdb']['value'] : each for each in data }.values()
    print(len(unique))
    with open(OUTFILE, 'w') as outfile:
        json.dump([u for u in unique], outfile)


