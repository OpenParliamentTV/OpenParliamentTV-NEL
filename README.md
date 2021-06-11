### Activate the virtual environment of your choice

e.g. via the command: pipenv shell

### Get dumps, e.g. members of German Bundestag:

1. python db_dump/queries/mdbs.py
2. python db_dump/scripts/mdbs/format.py
3. python db_dump/scripts/mdbs/remove_duplicates.py

Final json will be saved to:
db_dump/data/mdbs/mdbs-final.json
