import pygame
from constants import *
from highscore import *

# game over screen logic
def game_over(screen):

    # logic to return to main menu
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
        
        # screen and text info
        screen.fill((black))

        title_font = pygame.font.Font(None, 74)
        score_font = pygame.font.Font(None, 50)
        high_score = load_high_score()
        player_score = load_current_score()

        # text display parameters
        game_over_text = title_font.render("Game Over", True, (white))
        your_score_text = score_font.render(f"Your score: {player_score}", True, (white))
        high_score_text = score_font.render(f"High Score: {high_score}", True, (white))
        continue_text = score_font.render("Press Enter to Continue", True, (white))

        # draw text on screen with the above parameters
        screen.blit(game_over_text, (SCREEN_WIDTH/2 - game_over_text.get_width()/2, 150))
        screen.blit(your_score_text, (SCREEN_WIDTH/2 - your_score_text.get_width()/2, 250))
        screen.blit(high_score_text, (SCREEN_WIDTH/2 - high_score_text.get_width()/2, 320))
        screen.blit(continue_text, (SCREEN_WIDTH/2 - continue_text.get_width()/2, 450))

        pygame.display.flip()

    return "START_SCREEN"