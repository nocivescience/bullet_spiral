from manim import *
class Bullet(Triangle):
    CONFIG={
        'fill_opacity':1,
        'stroke_width':0,
        'length':0.1,
        'start_angle':PI,
        'aspect':1.5,
    }
    def __init__(self, **kwargs):
        Triangle.__init__(self, **kwargs)
        self.stretch_to_fit_height(self.CONFIG['aspect'])
        self.stretch_to_fit_width(.8)
        self.points[5:7]+=np.array([self.CONFIG['length'],0,0])
        self.scale(0.4)
    def get_angle2(self):
        return angle_of_vector(self.get_vector())
    def get_vector(self):
        return self.point_from_proportion(0.5)-self.get_start()
class BulletScene(Scene):
    def construct(self):
        vg1=VGroup()
        vg2=VGroup()
        self.an=0
        def update_bullet(obj,dt):
            obj.add(Bullet()).scale(0.7).rotate(PI*dt+self.an*10)
            for k in obj:
                k.shift(dt*20*np.array([
                    np.cos(k.get_angle2()),
                    np.sin(k.get_angle2()),
                    0
                ]))
                if abs(np.linalg.norm(k.get_center()-ORIGIN))>7:
                    obj.remove(k)
            self.an+=DEGREES
        def update_bullet_2(obj,dt):
            obj.add(Bullet()).scale(0.7).rotate(PI*dt*+self.an*10)
            for k in obj:
                k.shift(dt*20*np.array([
                    np.cos(k.get_angle2()),
                    np.sin(k.get_angle2()),
                    0
                ]))
                if abs(np.linalg.norm(k.get_center()-ORIGIN))>7:
                    obj.remove(k)
            self.an+=DEGREES
        vg1.add_updater(update_bullet)
        vg2.add_updater(update_bullet_2)
        self.add(vg1,vg2)
        self.wait(1)