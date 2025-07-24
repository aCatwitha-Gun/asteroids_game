import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # initialize all of pygame
    pygame.init()
    # set the display screen dimensions
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    # inifinit while loop used for the game loop
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill the screen with black
        screen.fill(black)

        # refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
