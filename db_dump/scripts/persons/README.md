# The scripts have to run in the following order:

1. format.py --> db_dump/data/persons/formatted.json
2. remove_duplicates.py --> db_dump/data/persons/deduped.json
3. enhance_with_external_data.py --> db_dump/data/persons/final.json

### Note that step 3 ( enhance_with_external_data.py) might take a few minutes because it is requesting other APIs
