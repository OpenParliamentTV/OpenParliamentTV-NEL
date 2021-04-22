### Activate the virtual environment of your choice

e.g. via the command: pipenv shell

### Get dumps in batches (takes a long time currently because queries are sequential)

python dump_batched.py

### Concat jsons

python ./db_dump/scripts/concat_jsons.py ./db_dump/data/mdbs/batches

### Remove duplicates

python ./db_dump/scripts/remove_duplicates.py ./db_dump/data/mdbs/batches_concatenated.json
