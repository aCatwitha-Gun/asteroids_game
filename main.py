import pygame
from constants import *
from player import Player

def main():
    # initialize all of pygame
    pygame.init()
    
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0

    # inifinit while loop used for the game loop
    while True:
        
        # enable the x to quit button on game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill the screen with black
        screen.fill("black")

        # draw player object
        player.draw(screen)

        # refresh the screen
        pygame.display.flip()

        # return delta time and limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
