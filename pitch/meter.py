import manim as mn
import logging

logger = logging.getLogger(__name__)


class PitchMeter(mn.VGroup):
    def __init__(self, scale: str, font_size=300):
        self.pitch_scale = mn.Text(f"1 = {scale}")
        self.prob_indicator = mn.Rectangle(
            stroke_width=0,
            fill_color=mn.BLUE,
            fill_opacity=1,
            width=0.3,
        )

        self.pitch_name = mn.Text("A", font_size=font_size)
        self.octave = mn.Text("4", font_size=font_size)
        self.sharp = mn.Text("#", font_size=font_size / 2)

        self.pitch_scale.to_corner(mn.UL)
        self.prob_indicator.stretch_to_fit_height(
            self.pitch_name.height + 1
        )
        self.main_group = (
            mn.VGroup(
                self.prob_indicator,
                self.pitch_name,
                self.octave,
            )
            .arrange(buff=1)
            .move_to(mn.ORIGIN + 0.3 * mn.LEFT)
        )
        self.sharp.next_to(self.main_group)
        self.sharp.align_to(self.main_group, mn.UP)

        self.bar = mn.Rectangle(
            width=self.main_group.width + 1.5,
            height=0.3,
        ).next_to(self.main_group, mn.DOWN)
        self.hz = mn.DecimalNumber(440).next_to(
            self.bar, mn.DOWN, buff=0.3
        )
        self.hz_text = mn.Text("Hz").next_to(self.hz)

        super().__init__(
            self.pitch_scale,
            self.prob_indicator,
            self.pitch_name,
            self.octave,
            self.sharp,
            self.bar,
            self.hz,
            self.hz_text,
        )

    def normalize(self):
        self.hz_text.next_to(self.hz)
