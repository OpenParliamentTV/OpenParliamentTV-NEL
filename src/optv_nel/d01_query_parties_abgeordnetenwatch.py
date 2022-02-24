from pathlib import Path
import json
import os
import optv_nel.abgeordnetenwatch.client as abgeordnetenwatch_client

OUTPATH = Path("data/01_raw/parties_abgeordnetenwatch")
OUTPATH.mkdir(parents=True, exist_ok=True)
OUTFILE = "parties.json"

parties = abgeordnetenwatch_client.get_parties()
with open(OUTPATH / Path(OUTFILE), 'w', encoding='utf8') as outfile:
    json.dump(parties, outfile, ensure_ascii=False)