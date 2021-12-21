This repository will contain NEL functionality for Open Parliament TV in the future. Right now it only generates custom Wikidata Dumps.

This README is not fully up to date and the repository is very much work in progress. We're working on updating it.

---

## Activate the virtual environment of your choice

e.g. via the command: pipenv shell

## Execute Wikidata queries:

(Order doesn't matter here)

### Persons:

python db_dump/queries/persons.py

### Parties:

python db_dump/queries/parties.py

### Factions:

python db_dump/queries/factions.py

## Execute Scripts to generate the final dumps:

Note: Order DOES matter here:

### 1. Parties:

Follow the README in db_dump/scripts/parties

### 2. Abgeordnetenwatch Mappings

python abgeordnetenwatch/scripts/generate_mapping.py

### 3. Mdbs

Follow the README in db_dump/scripts/mdbs

### 4. Factions

Follow the README in db_dump/scripts/factions

### 5. Other speakers

Follow the README in db_dump/scripts/other-speakers

#### Final json dumps will be saved to:

db_dump/data/mdbs/mdbs-final.json
db_dump/data/factions/factions-final.json
db_dump/data/parties/parties-final.json

### Notes about our approach:

- Our main source of data is Wikidata
- Sometimes Wikidata has weird information (e.g. parties of a mdb are not sorted or not complete. Factions are also problematic.), in this case we use Abgeordnetenwatch as a datasource, but map the IDs back to Wikidata
