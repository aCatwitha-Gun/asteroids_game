import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def game_loop(screen, dt):
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    clock = pygame.time.Clock()
    # inifinit while loop used for the game loop
    while True:
        
        # enable the x to quit button on game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

        updatable.update(dt)

        # collision check for player death
        for asteroid in asteroids.copy():
            if player.collision(asteroid):
                # check if player is invincible
                if not player.invincible_state:
                    player.life -= 1
                    player.start_invincibility()

                    # break the asteroid the player collided with
                    asteroid.split(asteroid.position)
                    player.explode()
                    
                    #return to menu if player is out of lives
                    if player.life <= 0:
                        return "START_SCREEN"

            # collision check for asteroid kill
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split(asteroid.position)
                    shot.kill()
                    player.score += 1
                    print(f"Player score: {player.score}")

        # fill the screen with black
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # draw player object
        player.draw(screen)

        # check for player rotation
        player.update(dt)

        # refresh the screen
        pygame.display.flip()

        # return delta time and limit framerate to 60 FPS
        dt = clock.tick(60) / 1000