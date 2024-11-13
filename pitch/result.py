import numpy as np
from pathlib import Path
from scipy.interpolate import CubicSpline
import pickle


def moving_average(x, w):
    return np.convolve(x, np.ones(w), "same") / w


class Result:
    def __init__(
        self,
        f0: np.ndarray,
        voiced_flag: np.ndarray,
        voiced_probs: np.ndarray,
        times: np.ndarray,
        md5: str,
    ) -> None:
        self.original_f0 = f0
        self.voiced_flag = voiced_flag
        self.original_voiced_probs = voiced_probs
        self.times = times
        self.md5 = md5

        self.valid_f0 = f0[voiced_flag]
        self.valid_times = times[voiced_flag]

        # self.valid_f0 = moving_average(self.valid_f0, 10)

        self.f0 = CubicSpline(
            self.valid_times, self.valid_f0
        )
        self.voiced_probs = CubicSpline(
            self.times, self.original_voiced_probs
        )
        self.time = times[-1]

    @staticmethod
    def load(file: Path) -> "Result":
        with open(file, "rb") as f:
            return pickle.load(f)

    def store(self, file: Path):
        with open(file, "wb") as f:
            pickle.dump(self, f)
