# No enhancing necessary, just copying over the file from previous step
import shutil
from pathlib import Path

SRC_PATH = "data/03_deduped/parties/parties.json"
DEST_FILENAME = "parties.json"
DEST_PATH = Path("data/05_enhanced/parties")
DEST_PATH.mkdir(parents=True, exist_ok=True)
shutil.copy(SRC_PATH, DEST_PATH / DEST_FILENAME )