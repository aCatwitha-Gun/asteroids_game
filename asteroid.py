from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self, position):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        pos_velocity = self.velocity.rotate(split_angle)
        neg_velocity = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_split_one = Asteroid(position.x, position.y, new_radius)
        asteroid_split_one.velocity = pos_velocity * 1.2

        asteroid_split_two = Asteroid(position.x, position.y, new_radius)
        asteroid_split_two.velocity = neg_velocity * 1.2
