import hashlib
from pathlib import Path


def calculate_md5(file: Path) -> str:
    with open(file, "rb") as f:
        data = f.read()
    return hashlib.md5(data).hexdigest()


def cache_file_of(music: Path) -> Path:
    stem = music.stem
    cache_file = f"{stem}.cache"
    return Path(music.parent / cache_file)


def has_cache(music: Path) -> bool:
    if not music.exists():
        return False

    hash_file = cache_file_of(music)
    if not hash_file.exists():
        return False

    return True
