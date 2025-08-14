import pygame
import math
from player import Player
from constants import *

# title screen logic
def start_screen(screen, dt):
    clock = pygame.time.Clock()
    # spawn player floating through space
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.rotation = 45

    # font for title text
    font = pygame.font.Font(None, 50)
    text = font.render("Press Space to Start", True, white)
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))

    # logic to start the game
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.kill()
                    waiting = False
        
        # player movement for visual on screen while waiting
        player.move(dt)
        player.screen_wrap()

        # title screen draw
        screen.fill(black)
        player.draw(screen)

        # blinking text logic
        if (pygame.time.get_ticks() // 500) % 2 == 1:
            screen.blit(text, text_rect)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    return True
