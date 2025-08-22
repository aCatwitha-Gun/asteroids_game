import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from title import start_screen
from gameloop import game_loop

def main():
    # initialize all of pygame
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    game_state = "START_SCREEN"

    while game_state != "QUIT":
        if game_state == "START_SCREEN":
            game_state = start_screen(screen, dt)
        elif game_state == "PLAYING":
            game_state = game_loop(screen, dt)

if __name__ == "__main__":
    main()
