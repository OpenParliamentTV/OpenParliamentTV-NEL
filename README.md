This repository will contain NEL functionality for Open Parliament TV in the future. Right now it only generates custom Wikidata Dumps.

This README is not fully up to date and the repository is very much work in progress. We're working on updating it.

---

## Activate the virtual environment of your choice

e.g. via the command: pipenv shell

## Execute Wikidata queries:

(Order doesn't matter here)

### Persons:

python src/optv_nel/queries/persons.py

### Parties:

python src/optv_nel/queries/parties.py

### Factions:

python src/optv_nel/queries/factions.py

## Execute Scripts to generate the final dumps:

Note: Order DOES matter here.
(Why? Parties need to be queried first, because AbgeordnetenWatch party mapping relies on this. And the 'enhance' script in Persons relies on this AbgeordnetenWatch party mapping.)

### 1. Parties:

Follow the README in db_dump/scripts/parties

### 2. Abgeordnetenwatch Mappings

python abgeordnetenwatch/scripts/generate_mapping.py

### 3. Persons

Follow the README in db_dump/scripts/persons

### 4. Factions

Follow the README in db_dump/scripts/factions

#### Final json dumps will be saved to:

db_dump/data/persons/final.json
db_dump/data/factions/factions-final.json
db_dump/data/parties/parties-final.json

### Notes about our approach:

- Our main source of data is Wikidata
- Sometimes Wikidata has insufficient information (e.g. parties and factions of a parliamentary member are not sorted or not complete.), in this case we use Abgeordnetenwatch as a datasource, but map the IDs back to Wikidata
