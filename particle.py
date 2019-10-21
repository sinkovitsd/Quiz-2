from Vec2 import Vec2


class Particle:
    def __init__(self, mass=float('inf'), pos=Vec2(0,0), vel=Vec2(0,0)):
        self.mass = mass
        self.pos = pos.copy()
        self.vel = vel.copy()
        self.force = Vec2(0,0)

    def update(self, dt):
        self.vel += self.force/self.mass*dt
        self.pos += self.vel*dt

    def update_vel(self, dt):
        self.vel += self.force/self.mass*dt

    def update_pos(self, dt):
        self.pos += self.vel*dt

    def clear_force(self):
        self.force = Vec2(0, 0)

    def add_force(self, force):
        self.force += force

    def apply_impulse(self, impulse):
        self.vel += impulse/self.mass
