import manim as mn
import logging
import librosa
import re
from .calc import percent_in_range

scale_position = mn.UL

logger = logging.getLogger(__name__)
pattern = re.compile(r"([A-G])(#?)([1-7])([+-])(\d+)")


class PitchMeter(mn.VGroup):
    def __init__(self, scale: str, font_size=300):
        self.pitch_scale = mn.Text(f"1 = {scale}")
        self.prob_indicator = mn.Rectangle(
            stroke_width=0,
            fill_color=mn.BLUE,
            fill_opacity=1,
            width=0.7,
        )

        self.font_size = font_size
        self.pitch_name = mn.Text("A", font_size=font_size)
        self.octave = mn.Text("4", font_size=font_size)
        self.sharp = mn.Text("#", font_size=font_size / 2)

        self.pitch_scale.to_corner(scale_position)
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
        self.sharp.next_to(self.pitch_name, buff=0.1)
        self.sharp.align_to(self.main_group, mn.UP)

        self.bar = (
            mn.Rectangle(
                width=self.main_group.width + 1.5,
                height=0.3,
            )
            .next_to(self.main_group, mn.DOWN)
            .set_fill(mn.WHITE, opacity=1)
        )

        self.triangle = (
            mn.Triangle()
            .scale(0.3)
            .set_fill(mn.BLUE, opacity=1)
            .move_to(
                self.bar.get_center()
                + self.bar.height * mn.DOWN
                + 0.3 * mn.DOWN
            )
        )

        self.lower_pitch_name = mn.Text("C2").next_to(
            self.bar, direction=mn.LEFT
        )
        self.upper_pitch_name = mn.Text("C5").next_to(
            self.bar, direction=mn.RIGHT
        )

        super().__init__(
            self.pitch_scale,
            self.prob_indicator,
            self.pitch_name,
            self.octave,
            self.sharp,
            self.bar,
            self.triangle,
            self.lower_pitch_name,
            self.upper_pitch_name,
        )

    def normalize(self):
        pass

    def set_status(self, hz: float, prob: float):
        self.prob_indicator.set_opacity(prob)
        if prob < 0.9:
            logger.info("not voicing, skip")
            return
        note = librosa.hz_to_note(
            hz, cents=True, unicode=False
        )
        sub_part = pattern.findall(note)
        logger.info(f"hz = {hz}, note = {note}")
        pitch_name, sharp, octave, pom, cent = sub_part[0]
        cent = int(cent)
        percent = percent_in_range(hz)
        logger.info(f"percent = {percent}")
        pitch_name = mn.Text(
            pitch_name, font_size=self.font_size
        ).move_to(self.pitch_name.get_center())
        octave = mn.Text(
            octave, font_size=self.font_size
        ).move_to(self.octave.get_center())
        if len(sharp) == 0:
            self.sharp.set_opacity(0)
        else:
            self.sharp.set_opacity(1)
        self.pitch_name.become(pitch_name)
        self.octave.become(octave)
        self.triangle.move_to(
            self.bar.get_left()
            + percent * mn.RIGHT * self.bar.width
            + mn.DOWN * self.bar.height
            + mn.DOWN * 0.3
        )
