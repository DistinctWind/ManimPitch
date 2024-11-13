from pathlib import Path
from pitch.calc import calculate_pitch
from pitch.meter import PitchMeter
import logging
import manim as mn
from pitch.animation import VisualizePitch

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s][%(levelname)s] %(message)s",
)

result = calculate_pitch(Path("vocal.wav"))


class TestScene(mn.Scene):
    def construct(self):
        pmeter = PitchMeter("C#")
        self.add(pmeter)
        self.play(
            VisualizePitch(
                pmeter,
                10,
                result.f0,
                result.voiced_probs,
            ),
            run_time=10,
            rate_func=mn.linear,
        )
        return super().construct()
