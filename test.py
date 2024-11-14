from pathlib import Path
from pitch.calc import calculate_pitch
from pitch.meter import PitchMeter
import logging
import manim as mn
from pitch.animation import VisualizePitch

file_path = "vocal.wav"
scale = "B"

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s][%(levelname)s] %(message)s",
)

result = calculate_pitch(Path(file_path))


class TestScene(mn.Scene):
    def construct(self):
        pmeter = PitchMeter(scale)
        self.add(pmeter)
        self.play(
            VisualizePitch(
                pmeter,
                result.time,
                result.f0,
                result.voiced_probs,
            ),
            run_time=result.time,
            rate_func=mn.linear,
        )
        return super().construct()
