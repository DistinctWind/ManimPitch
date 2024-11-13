from pitch.file import calculate_md5
from pitch.calc import calculate_pitch
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s][%(levelname)s] %(message)s",
)

print(calculate_md5(Path("vocal.wav")))
result = calculate_pitch(Path("vocal.wav"))
