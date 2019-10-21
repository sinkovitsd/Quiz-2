from particle import Particle
import pygame


class Circle(Particle):
    def __init__(self, radius=None, color=[0,0,0], width=0, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.color = color
        self.width = width

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos.int(), round(self.radius), self.width)

