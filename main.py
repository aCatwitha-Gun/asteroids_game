import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from title import start_screen

def main():
    # initialize all of pygame
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

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

    if start_screen(screen, dt):

        # inifinit while loop used for the game loop
        while True:
            
            # enable the x to quit button on game window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            updatable.update(dt)

            # collision check for player death
            for asteroid in asteroids:
                if player.collision(asteroid):
                    print("Game over!")
                    return
                # collision check for asteroid kill
                for shot in shots:
                    if shot.collision(asteroid):
                        asteroid.split(asteroid.position)
                        shot.kill()
    
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

if __name__ == "__main__":
    main()
