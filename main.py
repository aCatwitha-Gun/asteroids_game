import pygame
from constants import *
from player import Player
from asteroid import Asteroids

def main():
    # initialize all of pygame
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroids.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    # inifinit while loop used for the game loop
    while True:
        
        # enable the x to quit button on game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

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
