import pygame
from circle import Circle
from Vec2 import Vec2
import random
import colorsys
import math


def random_hsv_color(hlo, hhi, slo, shi, vlo, vhi):
    if hhi <  hlo:
        hhi += 1
    h = random.uniform(hlo, hhi)%1
    s = random.uniform(slo, shi)
    v = random.uniform(vlo, vhi)
    r, g, b = colorsys.hsv_to_rgb(h,s,v)
    return int(255*r), int(255*g), int(255*b)


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=[800, 600])
    bg_color = [255, 255, 255]
    screen.fill(bg_color)

    # List of objects in the game
    objects = []

    def setup(n):
        for i in range(n):
            radius = random.randint(15, 50)
            density = 1
            mass = density * 2 * math.pi * radius ** 2
            objects.append(Circle(mass=mass, radius=radius, color=random_hsv_color(0, 1, 1, 1, 1, 1), width=3,
                                  pos=Vec2(random.randint(radius, 800 - radius), random.randint(radius, 600 - radius))))

    setup(40)
    running = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1/fps

    # Game Loop
    while running:
        # Update display with what was drawn
        pygame.display.flip()

        # Wait
        clock.tick(fps) / 1000

        # Clear screen
        screen.fill(bg_color)

        # Move objects
        for o in objects:
            o.update(dt)

        # Event loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT: # user clicked close
                running = False

        # Draw objects to screen
        for o in objects:
            o.draw(screen)

    # Out of Game Loop, shut down pygame
    pygame.quit()


# safe start
if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()