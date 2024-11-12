import hashlib
from pathlib import Path


def calculate_md5(file_path: Path) -> str:
    with open(file_path, "rb") as f:
        data = f.read()
    return hashlib.md5(data).hexdigest()


def hash_file_of(music_path: Path) -> Path:
    stem = music_path.stem
    hash_file = f"{stem}.rmd5"
    return Path(music_path.parent / hash_file)


def result_file_of(music_path: Path) -> Path:
    stem = music_path.stem
    result_file = f"{stem}.npz"
    return Path(music_path.parent / result_file)


def has_cache(music_path: Path) -> bool:
    if not music_path.exists():
        return False

    hash_file = hash_file_of(music_path)
    if not hash_file.exists():
        return False

    with open(hash_file, "r") as hf:
        hash = hf.read()
    cur_hash = calculate_md5(music_path)
    return cur_hash == hash


def mark_cached(music_path: Path):
    hash_file = hash_file_of(music_path)
    with open(hash_file, "w") as hf:
        hf.write(calculate_md5(music_path))
