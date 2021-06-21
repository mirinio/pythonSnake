from settings import *
import pygame
import time 
# Define some colors
GREEN = ( 146, 208, 81)
BORDER = (154,115,96)
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)

class Menu:
    def __init__(self, game):
        self.game = game
        self.run_display = True

        self.size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.myfont = pygame.font.SysFont(self.game.font_name, 25)
   
    def show(self):
        self.run_display = True
        self.game.render_background()

        while self.run_display:
            self.game.check_events()
            if self.game.state == "GAMEOVER":
               self.display_gameover()
            else:
                self.draw_menu()
            pygame.display.update()
        
    def display_gameover(self):
        font = pygame.font.SysFont(self.game.font_name, 80)
        game_over_txt = font.render(f"GAME OVER", True, (255, 255, 255))
        self.game.screen.blit(game_over_txt, (SCREEN_WIDTH*0.5/2, SCREEN_HEIGHT/3))
        font_txt = pygame.font.SysFont(self.game.font_name, 50)
        score_txt = font_txt.render(f"SCORE {self.game.snake.length}", True, (255, 255, 255))
        self.game.screen.blit(score_txt, (SCREEN_WIDTH*0.5/2, SCREEN_HEIGHT*1.25/3))
        again_txt = font_txt.render("To play again press Enter. To exit press Escape", True, (255, 255, 255))
        self.game.screen.blit(again_txt, (SCREEN_WIDTH*0.5/2, SCREEN_HEIGHT*1.5/3))
        

    def get_highscore(self):
        with open('highscore.txt', 'r') as f:
            l = [line.strip('\n').split(',') for line in f]
            return l

    def start_game(self):
        self.run_display = False
        self.game.playing = True
        self.game.init_start()

    def quit_game(self):
        self.game.playing = False
        self.game.running = False
        pygame.quit()



    def draw_menu(self):
        self.draw_button(self.game.screen, BLACK, [self.size[0]/2 - 75, 30, 150, 50], 2, BORDER, 'Beach Snake')
        self.draw_button(self.game.screen, BLACK, [self.size[0]/3 - 75, self.size[1] - 150, 150, 50], 2, BORDER, 'Start', self.start_game)
        self.draw_button(self.game.screen, BLACK, [self.size[0]/3*2 - 75, self.size[1] - 150, 150, 50], 2, BORDER, 'Exit', self.quit_game)
        scores = self.get_highscore()
        self.draw_highscore(self.game.screen, BLACK, [self.size[0]/2 - self.size[0]/4, self.size[1]/2 - self.size[1]/4, self.size[0]/2, self.size[1]/2], 2, BORDER, scores)

    def draw_rect_border(self, screen, fillColor, sizePos, borderWidth, borderColor):
        pygame.draw.rect(screen, borderColor, sizePos)
        pygame.draw.rect(screen, fillColor, [sizePos[0] + borderWidth, sizePos[1] + borderWidth, sizePos[2] - borderWidth*2, sizePos[3] - borderWidth*2])

    def draw_button(self, screen, fillColor, sizePos, borderWidth, borderColor, text, callback = None):
        button = self.draw_rect_border(screen, fillColor, sizePos, borderWidth, borderColor)
        my_text = self.myfont.render(text, False, WHITE)
        text_width = my_text.get_width()
        text_height = my_text.get_height()
        screen.blit(my_text,(sizePos[0] + sizePos[2]/2 - text_width/2,sizePos[1] + sizePos[3]/2 - text_height/2))
        
        mPos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and mPos[0] > sizePos[0] and mPos[0] < (sizePos[0] + sizePos[2]) and mPos[1] > sizePos[1] and mPos[1] < (sizePos[1] + sizePos[3]):
            if callable(callback):
                callback()

    def draw_highscore(self, screen, fillColor, sizePos, borderWidth, borderColor, scores):
        topScorer_height = 50
        self.draw_rect_border(screen, fillColor, sizePos, borderWidth, borderColor)
        self.draw_button(screen, BLACK, [sizePos[0], sizePos[1],sizePos[2], topScorer_height], 2, BORDER, 'Top scorer')
        for i, array_el in enumerate(scores):
            col_1_rank = self.myfont.render(array_el[0], False, WHITE)
            col_2_name = self.myfont.render(array_el[1], False, WHITE)
            col_3_score = self.myfont.render(array_el[2], False, WHITE)
            screen.blit(col_1_rank,[sizePos[0] + 30,sizePos[1] + topScorer_height + 30 + (i * 30)])
            screen.blit(col_2_name,[sizePos[0] + 60 + sizePos[3] / 3,sizePos[1] + topScorer_height + 30 + (i * 30)])
            screen.blit(col_3_score,[sizePos[0] + 90 + sizePos[3] / 3 * 2,sizePos[1] + topScorer_height + 30 + (i * 30)])

