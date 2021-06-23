from settings import *
import pygame
import time 

class Menu:
    """Menu Klasse für das Python Game"""
    def __init__(self, game):
        self.game = game
        self.run_display = True

        self.size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.myfont = pygame.font.SysFont(self.game.font_name, 25)
   
    def show(self):
        """Menu renderinng je nach menu status"""
        self.run_display = True
        inputbox = InputBox(SCREEN_WIDTH/3,SCREEN_HEIGHT/3,500,125, self.game,"Enter Name")
        scores = self.get_highscore()
        if self.game.state == "GAMEOVER":
            self.set_highscore(scores)

        while self.run_display:
            self.game.check_events(inputbox)
            self.game.render_background()    
            if self.game.state == "GAMEOVER":
               self.display_gameover()
            elif self.game.state == "MENU":
                self.draw_menu(scores)
            elif self.game.state == "ENTERNAME":
                inputbox.draw()
                inputbox.update()    
           
            elif self.game.state == "PLAY":
                self.start_game()        

            pygame.display.update()

    def display_gameover(self):
        """ Gameover menu wird gerendert """
        font = pygame.font.SysFont(self.game.font_name, 80)
        game_over_txt = font.render(f"GAME OVER", True, (255, 255, 255))
        
        self.game.screen.blit(game_over_txt, (SCREEN_WIDTH*0.5/2, SCREEN_HEIGHT/3))
        font_txt = pygame.font.SysFont(self.game.font_name, 50)
        
        score_txt = font_txt.render(f"SCORE {self.game.snake.length}", True, (255, 255, 255))
        self.game.screen.blit(score_txt, (SCREEN_WIDTH*0.5/2, SCREEN_HEIGHT*1.25/3))
        
        again_txt = font_txt.render("To play again press Enter. To exit press Escape", True, (255, 255, 255))
        self.game.screen.blit(again_txt, (SCREEN_WIDTH*0.5/2, SCREEN_HEIGHT*1.5/3))
        

    def get_highscore(self):
        """Highscores aus dem highscore.txt laden"""
        with open('highscore.txt', 'r') as f:
            l = [line.strip('\n').split(',') for line in f]
            return l
    
    def set_highscore(self, scores):
        """Highscore updaten im highscore.txt"""
        scores.append([str(self.game.snake.length), self.game.player_name])
        
        sorted_scores = sorted(scores, key=lambda x: int(x[0]), reverse=True)

        with open('highscore.txt', 'r+') as f:
            f.truncate(0)
            for i, player in enumerate(sorted_scores):
                f.write(player[0] + "," + player[1] + "\n")
                if i == 10:
                    break

    def start_game(self):
        """leitet den spiel start in gang mittels 
        parameter und player sowie item initialisierung
        """
        self.run_display = False
        self.game.playing = True
        self.game.state = "PLAY"
        self.game.init_start()

    def set_enter_name_state(self):
        """game status auf entername stellen für das feld"""
        self.game.state = "ENTERNAME"


    def quit_game(self):
        """stoppt das spiel"""
        self.game.playing = False
        self.game.running = False
        pygame.quit()

    def draw_menu(self,scores):
        """Rendert das Menu mit dem highscore,start, exit"""
        self.draw_button(self.game.screen, BLACK, [self.size[0]/2 - 75, 30, 150, 50], 2, BORDER, 'Beach Snake')
        self.draw_button(self.game.screen, BLACK, [self.size[0]/3 - 75, self.size[1] - 150, 150, 50], 2, BORDER, 'Start', self.set_enter_name_state)
        self.draw_button(self.game.screen, BLACK, [self.size[0]/3*2 - 75, self.size[1] - 150, 150, 50], 2, BORDER, 'Exit', self.quit_game)
        self.draw_highscore(self.game.screen, BLACK, [self.size[0]/2 - self.size[0]/4, self.size[1]/2 - self.size[1]/4, self.size[0]/2, self.size[1]/2], 2, BORDER, scores)

    def draw_rect_border(self, screen, fillColor, sizePos, borderWidth, borderColor):
        """zeichnet ein rechteckt"""
        pygame.draw.rect(screen, borderColor, sizePos)
        pygame.draw.rect(screen, fillColor, [sizePos[0] + borderWidth, sizePos[1] + borderWidth, sizePos[2] - borderWidth*2, sizePos[3] - borderWidth*2])

    def draw_button(self, screen, fillColor, sizePos, borderWidth, borderColor, text, callback = None):
        """zeichnet einen Knopf"""
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
        """zeichnet den highscore"""
        topScorer_height = 50
        self.draw_rect_border(screen, fillColor, sizePos, borderWidth, borderColor)
        self.draw_button(screen, BLACK, [sizePos[0], sizePos[1],sizePos[2], topScorer_height], 2, BORDER, 'Top scorer')
        for i, array_el in enumerate(scores):
            col_2_name = self.myfont.render(array_el[0], False, WHITE)
            col_3_score = self.myfont.render(array_el[1], False, WHITE)
            screen.blit(col_2_name,[sizePos[0] + 60 + sizePos[3] / 3,sizePos[1] + topScorer_height + 30 + (i * 30)])
            screen.blit(col_3_score,[sizePos[0] + 90 + sizePos[3] / 3 * 2,sizePos[1] + topScorer_height + 30 + (i * 30)])


class InputBox:
    """Input Feld Klasse um namen einzugeben"""

    def __init__(self, x, y, w, h, game, text=''):
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (199, 199, 199)
        self.text = text
        self.font = pygame.font.SysFont('arial', 80)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """behandelt alle events für die eingabe im Input feld"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
                self.text = ''
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = (173, 144, 102) if self.active else (199, 199, 199)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.game.player_name = self.text
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        """Macht die box grösser wenn der text länder als das rechteck ist"""
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self):
        """rendert den text und das rechteck"""
        self.game.screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(self.game.screen, self.color, self.rect, 2)