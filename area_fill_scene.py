from base_oscillation_scene import BaseOscillation

from manim import *


class CircleOscillationScene(BaseOscillation):
    def __init__(self):
        super().__init__()

        self.x_phi_0 = PI / 3
        self.x_radius = 2
        self.x_w = 10.0

        self.y_phi_0 = PI / 4
        self.y_radius = 1.5
        self.y_w = 16.18  # Golden ratio
