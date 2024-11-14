import manim as mn
from .meter import PitchMeter


class VisualizePitch(mn.Animation):
    def __init__(
        self,
        meter: PitchMeter,
        time: float,
        f0,
        voiced_prob,
        **kwargs,
    ):
        self.meter = meter
        self.time = time
        self.f0 = f0
        self.voiced_prob = voiced_prob
        super().__init__(meter, **kwargs)

    def interpolate_mobject(self, alpha: float) -> None:
        current = self.time * alpha
        current_f0 = self.f0(current)
        current_prob = self.voiced_prob(current)
        self.meter.set_status(current_f0, current_prob)
