from manim import *

from objects.angle_circle import AngleCircle
from objects.moving_dot import MovingDot


class SimpleOscillation(Scene):
    def construct(self):
        x_phi_0 = PI / 4 + PI / 2
        x_radius = 2
        x_w = 1

        y_phi_0 = PI / 4
        y_radius = 2
        y_w = 2

        # First oscillator
        y_formula = MathTex(r"y(t)=A_y\sin(\omega_y t+\phi_y)")

        self.play(Write(y_formula))

        y_angle_circle = AngleCircle(
            radius=y_radius, phi_0=y_phi_0, arc_offset=0, label=r"\phi_y"
        )

        self.play(
            Create(y_angle_circle),
            y_formula.animate.scale(0.75).next_to(y_angle_circle, DOWN, buff=1),
        )

        self.play(
            y_angle_circle.angle_tracker.animate.set_value(TAU * 2 * y_w + y_phi_0),
            run_time=8,
        )
        y_angle_circle.angle_tracker.set_value(y_phi_0)

        y_moving_dot = MovingDot(
            rotation=PI / 2,
            length=y_radius * 2,
            dot_y=lambda: y_angle_circle.arrow.get_end()[1],
        )

        y_moving_dot.next_to(y_angle_circle.circle, RIGHT, buff=1)

        self.play(Create(y_moving_dot))

        self.play(
            y_angle_circle.angle_tracker.animate.set_value(TAU * 2 * y_w + y_phi_0),
            run_time=8,
        )
        y_angle_circle.angle_tracker.set_value(y_phi_0)

        group_y = VGroup(y_angle_circle, y_moving_dot)

        y_moving_dot.remove_updaters()
        y_angle_circle.remove_updaters()
        self.play(
            group_y.animate.scale(0.5).shift(LEFT * 5.0 + UP * 2.0),
            y_formula.animate.to_edge(UR).shift(DOWN + LEFT * 0.5),
        )

        # Second oscillator
        x_formula = MathTex(r"x(t)=A_x\sin(\omega_x t+\phi_x)")

        self.play(Write(x_formula))

        x_angle_circle = AngleCircle(
            radius=x_radius, phi_0=x_phi_0, arc_offset=PI / 2, label=r"\phi_x"
        )

        self.play(
            Create(x_angle_circle),
            x_formula.animate.scale(0.75).next_to(x_angle_circle, DOWN, buff=1),
        )

        self.play(
            x_angle_circle.angle_tracker.animate.set_value(TAU * 2 * x_w + x_phi_0),
            run_time=8,
        )
        x_angle_circle.angle_tracker.set_value(x_phi_0)

        x_moving_dot = MovingDot(
            rotation=0,
            length=x_radius * 2,
            dot_x=lambda: x_angle_circle.arrow.get_end()[0],
        )

        x_moving_dot.next_to(x_angle_circle.circle, UP, buff=1)

        self.play(Create(x_moving_dot))

        self.play(
            x_angle_circle.angle_tracker.animate.set_value(TAU * 2 * x_w + x_phi_0),
            run_time=8,
        )
        x_angle_circle.angle_tracker.set_value(x_phi_0)

        group_x = VGroup(x_angle_circle, x_moving_dot)

        x_moving_dot.remove_updaters()
        x_angle_circle.remove_updaters()
        self.play(
            group_x.animate.scale(0.5),
            x_formula.animate.next_to(y_formula, DOWN, buff=MED_SMALL_BUFF),
        )
        self.play(group_x.animate.next_to(y_moving_dot.number_line, DR, buff=0))

        self.wait(1)

        group_xy = VGroup(group_x, group_y)

        self.play(group_xy.animate.scale(1.5).move_to(ORIGIN).shift(LEFT * 3.0))

        x_moving_dot.add_updaters()
        x_angle_circle.add_updaters()
        y_moving_dot.add_updaters()
        y_angle_circle.add_updaters()

        self.wait(1)

        dot = Dot()

        dot.add_updater(
            lambda a: a.move_to(
                np.array(
                    [
                        x_angle_circle.arrow.get_end()[0],
                        y_angle_circle.arrow.get_end()[1],
                        0,
                    ]
                )
            )
        )

        traced_path = TracedPath(
            dot.get_center,
            dissipating_time=1,
            stroke_color=RED,
            stroke_width=4,
            stroke_opacity=[1, 0],
        )

        self.add(dot, traced_path)

        self.play(
            x_angle_circle.angle_tracker.animate.set_value(TAU * 2 * x_w + x_phi_0),
            y_angle_circle.angle_tracker.animate.set_value(TAU * 2 * y_w + y_phi_0),
            run_time=12,
        )

        self.wait(1)
