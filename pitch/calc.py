import librosa
import logging
import math
from pathlib import Path
from .result import Result
from .file import has_cache, cache_file_of, calculate_md5

logger = logging.getLogger(__name__)

C2_hz = float(librosa.note_to_hz("C2"))
C5_hz = float(librosa.note_to_hz("C5"))


def percent_in_range(f: float):
    f_min = C2_hz
    f_max = C5_hz

    N = 12 * math.log2(f_max / f_min)
    n = 12 * math.log2(f / f_min)

    percent = n / N
    return percent


def calculate_pitch(music: Path) -> Result:
    logger.info(f"Calculate pitch for file {music}")
    cache_file = cache_file_of(music)
    md5 = calculate_md5(music)
    logger.debug(f"Md5 for file {music} is '{md5}'")

    if has_cache(music):
        cache = Result.load(cache_file)
        if md5 == cache.md5:
            logger.info(f"Use cache for file {music}")
            return cache
        logger.info(
            f"Cache file for file {music} is outdated"
        )

    logger.info("Recalculate pitch for file {music}")
    y, sr = librosa.load(music, sr=None)
    f0, voiced_flag, voiced_probs = librosa.pyin(
        y,
        sr=sr,
        fmin=C2_hz,
        fmax=C5_hz,
    )
    times = librosa.times_like(f0, sr=sr)
    result = Result(
        f0=f0,
        voiced_flag=voiced_flag,
        voiced_probs=voiced_probs,
        times=times,
        md5=md5,
    )

    logger.info(f"Store cache into file {cache_file}")
    result.store(cache_file)
    return result
