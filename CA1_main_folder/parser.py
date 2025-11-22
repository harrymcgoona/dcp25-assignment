from pathlib import Path
from typing import List, Dict

def parse_abc_file(file_path: Path) -> List[Dict]:
  tunes = []
  with open(file_path, "r") as f:
    content = f.read()

  raw_tunes = content.split("\n\n")

  for raw in raw_tunes:
    tune = {}
    for line in raw.splitlines():
      line = line.strip()
      if line.startswith("T:"):
        tune["title"] = line[2:].strip()
      elif line.startswith("R:"):
        tune["type"] = line[2:].strip()
      elif line.startswith("M:"):
        tune["meter"] = line[2:].strip()
      elif line.startswith("K:"):
        tune["key"] = line[2:].strip()
      elif line.startswith("L:"):
        tune["default_note_length"] = line[2:].strip()

    if tune:
      tunes.append(tune)

  return tunes
