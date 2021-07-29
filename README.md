## Activate the virtual environment of your choice

e.g. via the command: pipenv shell

## Excecute Wikidata queries:

(Order doesn't matter here)

### MdBs:

python db_dump/queries/mdbs.py

### Parties:

python db_dump/queries/parties.py

### Factions:

python db_dump/queries/factions.py

## Excecute Scripts to generate the final dumps:

Note: Order DOES matter here:

### 1. Parties:

Follow the README in db_dump/scripts/parties

### 2. Algorithmwatch Mappings

python abgeordnetenwath/scripts/generate_mapping.py

### 3. Mdbs

Follow the README in db_dump/scripts/parties

### 4. Factions

Follow the README in db_dump/scripts/factions

#### Final json dumps will be saved to:

db_dump/data/mdbs/mdbs-final.json
db_dump/data/factions/factions-final.json
db_dump/data/parties/parties-final.json

### Notes about our approach:

- Our main source of data is WikiData
- Sometimes WikiData has weird information (e.g. parties of a mdb are not sorted or not complete. Factions are also problematic.), in this case we use AbgeordnetenWatch as a datasource, but map the ids back to WikiData
