from base_oscillation_scene import BaseOscillation

from manim import *


class Lissajous2By3Scene(BaseOscillation):
    def __init__(self):
        super().__init__()

        self.x_phi_0 = 0
        self.x_radius = 2
        self.x_w = 2

        self.y_phi_0 = 0
        self.y_radius = 2
        self.y_w = 3
