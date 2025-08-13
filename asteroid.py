from circleshape import CircleShape
import pygame

class Asteroids(CircleShape):
    def __init__(self, x, y, position, radius, velocity):
        super().__init__(x, y, radius, position, velocity)

    def draw(self):
        pygame.draw.circle(self, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt