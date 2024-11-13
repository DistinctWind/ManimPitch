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
        pmeter = PitchMeter("B")
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
