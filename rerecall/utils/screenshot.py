from dataclasses import dataclass
from typing import List
from mss import mss
from pathlib import Path
from base64 import b64encode

@dataclass
class Screenshot():
  filename: str
  base64: bytes

def get_screenshots(timestamp: str) -> List[Screenshot]:
  screenshots: List[Screenshot] = []
  with mss(with_cursor=True, compression_level= 9) as sct:
    for file in sct.save(output=f"screenshots/{timestamp}-monitor-{{mon}}.png"):
      base64 = b64encode(Path(file).read_bytes())
      screenshots.append(Screenshot(filename=file, base64=base64))
  return screenshots
