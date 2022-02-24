# No deduping necessary, just copying over the file from previous step
import shutil
from pathlib import Path

SRC_PATH = "data/02_formatted/factions/factions.json"
DEST_FILENAME = "factions.json"
DEST_PATH = Path("data/03_deduped/factions")
DEST_PATH.mkdir(parents=True, exist_ok=True)
shutil.copy(SRC_PATH, DEST_PATH / DEST_FILENAME )