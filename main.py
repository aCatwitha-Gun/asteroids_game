import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from title import start_screen
from gameloop import game_loop
from gameover import game_over


def main():
    # initialize all of pygame
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    # default game state
    game_state = "START_SCREEN"

    # game states that are changed when the current game state function returns another value.
    while game_state != "QUIT":
        if game_state == "START_SCREEN":
            game_state = start_screen(screen, dt)
        elif game_state == "PLAYING":
            game_state = game_loop(screen, dt)
        elif game_state == "GAME_OVER":
            game_state = game_over(screen)

if __name__ == "__main__":
    main()
