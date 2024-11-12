import librosa
from pathlib import Path
from .result import Result
from .file import has_cache, mark_cached, result_file_of


def calculate_pitch(music: Path) -> Result:
    result_file = result_file_of(music)
    if has_cache(music):
        return Result.load(result_file)

    # No cache, must calc
    y, sr = librosa.load(music, sr=None)
    C2_hz = float(librosa.note_to_hz("C2"))
    C7_hz = float(librosa.note_to_hz("C7"))
    f0, voiced_flag, voiced_probs = librosa.pyin(
        y,
        sr=sr,
        fmin=C2_hz,
        fmax=C7_hz,
    )
    times = librosa.times_like(f0, sr=sr)
    result = Result(
        f0=f0,
        voiced_flag=voiced_flag,
        voiced_probs=voiced_probs,
        times=times,
    )

    mark_cached(music)
    result.store(result_file)
    return result
