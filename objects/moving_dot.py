from manim import *


class MovingDot(VGroup):
    def remove_updaters(self):
        self.dot.clear_updaters()

    def add_updaters(self):
        self.dot.add_updater(
            lambda a: a.move_to(
                np.array(
                    [
                        self.dot_x(),
                        self.dot_y(),
                        0,
                    ]
                )
            )
        )

    def __init__(self, rotation, length, dot_x=None, dot_y=None):
        super().__init__()

        self.number_line = NumberLine(
            x_range=[0, length, 1], length=length, rotation=rotation, color=WHITE
        )

        self.dot_x = lambda: self.number_line.get_center()[0] if dot_x is None else dot_x()
        self.dot_y = lambda: self.number_line.get_center()[1] if dot_y is None else dot_y()

        self.dot = Dot(
            point=np.array(
                [
                    self.dot_x(),
                    self.dot_y(),
                    0,
                ]
            ),
            color=RED,
        )

        self.add_updaters()

        self.add(self.number_line, self.dot)

    @override_animation(Create)
    def create(self):
        return Succession(Create(self.number_line), Create(self.dot))
