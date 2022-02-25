This repository will contain NEL functionality for Open Parliament TV in the future. Right now it only generates custom Wikidata Dumps.

This README is not fully up to date and the repository is very much work in progress. We're working on updating it.

---

## Install dependencies

pipenv install

## Activate the virtual environment

pipenv shell

## Execute scripts

Excecute scripts (`python src/optv_nel/{scriptname}`) in the order of the prefixed number:

```
d01_...
d02_...
d03_...
d04_...
d05_...
```

The order within these groups doesn't matter (e.g. `d01_query_factions.py` doesnt need to come before `d01_query_parties.py`)

The script filename prefix corresponds to the output filname prefix, e.g.
Scripts starting with `d01_` will output into the folder `data/01_`

### Notes about our approach:

- Our main source of data is Wikidata
- Sometimes Wikidata has insufficient information (e.g. parties and factions of a parliamentary member are not sorted or not complete.), in this case we use Abgeordnetenwatch as a datasource, but map the IDs back to Wikidata
