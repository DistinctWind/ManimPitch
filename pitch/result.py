import numpy as np
from pathlib import Path


class Result:
    def __init__(
        self,
        f0: np.ndarray,
        voiced_flag: np.ndarray,
        voiced_probs: np.ndarray,
        times: np.ndarray,
    ) -> None:
        self.f0 = f0
        self.voiced_flag = voiced_flag
        self.voiced_probs = voiced_probs
        self.times = times

    @staticmethod
    def load(file: Path) -> "Result":
        cache = np.load(file)

        return Result(
            f0=cache["f0"],
            voiced_flag=cache["voiced_flag"],
            voiced_probs=cache["voiced_probs"],
            times=cache["times"],
        )

    def store(self, file: Path):
        np.savez(
            file,
            f0=self.f0,
            voiced_flag=self.voiced_flag,
            voiced_probs=self.voiced_probs,
            times=self.times,
        )
