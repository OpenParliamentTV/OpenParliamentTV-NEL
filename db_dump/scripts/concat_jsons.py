import sys
import os
import json

#FOLDER = './db_dump/mdbs_batched_by_year_of_birth'
FOLDER = sys.argv[1]
OUTFILE = os.path.splitext(FOLDER)[0] + "_concatenated.json"
try:
    OUTFILE = sys.argv[2]
except:
    print("Output file saved as: ", OUTFILE)

files = [os.path.join(FOLDER, f) for f in os.listdir(FOLDER)]

with open(OUTFILE, 'a') as writer:
    writer.write('[')
    for i, f in enumerate(files):
        with open(f) as reader:
            content = json.load(reader)
            data = content['results']['bindings']
            for j, d in enumerate(data):
                json.dump(d, writer)
                if i < len(files) - 1 or j < len(data) - 1:
                    writer.write(',')
    writer.write(']')          


    