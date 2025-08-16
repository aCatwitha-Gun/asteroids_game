import pygame
import random
from circleshape import CircleShape
from constants import *
from shot import Shot

# class to hold death effect particle system
class Particle():
    def __init__(self, p1, p2, velocity):
        self.p1 = pygame.math.Vector2(p1)
        self.p2 = pygame.math.Vector2(p2)
        self.velocity = pygame.math.Vector2(velocity)

    def update(self):
        self.p1 += self.velocity
        self.p2 += self.velocity

# base class for player object
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.is_exploding = False
        self.explosion_particles = []
        self.explosion_speed = PLAYER_DEATH_SPEED
        self.explosion_timer = 0
        self.life = 3

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    # draw method override
    def draw(self, screen):
        # draw death animation if is_exploding
        if self.is_exploding:
            if self.explosion_timer > 0:
                for particle in self.explosion_particles:
                    pygame.draw.aaline(screen, "white", particle.p1, particle.p2)
        else:
            pygame.draw.polygon(screen, "white", self.triangle(), 2)

    
    # allows player to wrap around screen edges
    def screen_wrap(self):
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT

    # player rotate speed
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # update method override
    def update(self, dt):
        if self.is_exploding:
            # update the explosion animation
            if self.explosion_timer > 0:
                self.explosion_timer -= 1
                for particle in self.explosion_particles:
                    particle.update()
            else:
                self.is_exploding = False
        else:
            self.shot_cooldown -= dt
            self.screen_wrap()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                self.rotate(-dt)
            if keys[pygame.K_d]:
                self.rotate(dt)
            if keys[pygame.K_w]:
                self.move(dt)
            if keys[pygame.K_s]:
                self.move(-dt)
            if keys[pygame.K_SPACE]:
                self.shoot()

    # player movement math
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # player shot mechanic
    def shoot(self):
        shot_cooldown = self.shot_cooldown
        if shot_cooldown > 0:
            return
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
    
    # player death animation
    def explode(self):
        if self.is_exploding:
            return
        
        self.is_exploding = True
        self.explosion_timer = self.explosion_speed
        self.explosion_particles = []

        # get player object shape info
        points = self.triangle()

        #create particles for each side of the triangle
        for i in range(len(points)):
            p1 = points[i]
            p2 = points[(i + 1) % len(points)]

            # calculate velocity from ship's center
            mid_point = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
            velocity = (pygame.math.Vector2(mid_point) - self.position).normalize()
            velocity *= random.uniform(1.5, 3.0)

            self.explosion_particles.append(Particle(p1, p2, velocity))