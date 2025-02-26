from manim import *
from numpy import sqrt


class AngleCircle(VGroup):
    def remove_updaters(self):
        self.arrow.clear_updaters()
        self.arc.clear_updaters()

    def add_updaters(self):
        self.arrow.add_updater(
            lambda a: a.put_start_and_end_on(
                self.circle.get_center(),
                self.circle.point_at_angle(self.angle_tracker.get_value()),
            )
        )

        x = self.circle.get_center().real
        y = self.circle.point_at_angle(self.angle_tracker.get_value()).real

        self.arc.add_updater(
            lambda a: a.become(
                Arc(
                    radius=sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) / 4,
                    angle=(self.angle_tracker.get_value() - self.arc_offset) % (2 * PI),
                    color=GREEN,
                    fill_color=GREEN,
                    start_angle=self.arc_offset,
                    arc_center=self.circle.get_center(),
                )
            )
        )

    def __init__(self, radius, phi_0, arc_offset, label):
        super().__init__()

        self.radius = radius
        self.phi_0 = phi_0
        self.arc_offset = arc_offset

        self.circle = Circle(radius=radius, color=WHITE)

        self.angle_tracker = ValueTracker(phi_0)

        self.arrow = Arrow(
            start=self.circle.get_center(),
            end=self.circle.point_at_angle(self.angle_tracker.get_value()),
            buff=0,
            color=YELLOW,
            stroke_width=4,
        )

        self.arc = Arc(
            radius=radius / 4,
            angle=(self.angle_tracker.get_value() - arc_offset) % (2 * PI),
            color=GREEN,
            fill_color=GREEN,
            start_angle=arc_offset,
            arc_center=self.circle.get_center(),
        )

        self.label = MathTex(label, font_size=36 * radius / 2).move_to(
            Arc(
                radius=radius / 2.6,
                angle=(self.angle_tracker.get_value() - arc_offset) % (2 * PI),
                start_angle=arc_offset,
                arc_center=self.circle.get_center(),
            ).point_from_proportion(0.5)
        )

        self.add_updaters()

        self.add(self.circle, self.arc, self.label, self.arrow)

    @override_animation(Create)
    def create_override(self):
        return Succession(
            Create(self.circle),
            Create(self.arrow),
            AnimationGroup(Create(self.arc), Write(self.label)),
        )
