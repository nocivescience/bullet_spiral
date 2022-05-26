from manim import *
class Bullet(Triangle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_fill(color=BLACK, opacity=1)
        self.set_stroke(color=BLACK, width=1)
        self.set_height(0.2)
        self.set_width(0.2)
        self.move_to(np.array([0, 0, 0]))
        self.set_fill(BLACK, 1)
        self.set_stroke(BLACK, 1)
        self.set_height(0.2)
        self.set_width(0.2)
        self.move_to(np.array([0, 0, 0]))
class BulletScene(Scene):
    def construct(self):
        bullet=Bullet()
        self.add(bullet)
        self.wait(2)