from pitch.file import calculate_md5
from pitch.calc import calculate_pitch
from pathlib import Path

print(calculate_md5(Path("vocal.wav")))
result = calculate_pitch(Path("vocal.wav"))
print(result.time)
