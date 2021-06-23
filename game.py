import pygame
import time 
from pygame.locals import *

from snake import Snake
from items import ItemManager
from settings import *
from view import *

class Game:
    def __init__(self):
        pygame.init() 
        
        self.font_name = 'arial'

        pygame.mixer.init()
       
        pygame.display.set_caption("Beach Snake")
        self.display = pygame.Surface(SCREEN_SIZE)
        self.screen = pygame.display.set_mode(SCREEN_SIZE) 
        self.render_background()
        pygame.display.flip()

        self.menu = Menu(self)
        self.running = True
        self.playing = False
        self.state = "MENU"
        self.player_name = ""
    
    def render_background(self):
        bg = pygame.image.load("resources/beach.jpg")
        self.screen.blit(bg, (0,0))

    def game_Logic(self):
      

        for item in self.itemManager.items:
            if self.is_collision(self.snake.x[0], self.snake.y[0], item.x, item.y):
                #sound = pygame.mixer.Sound("resources/eat.mp3")
                #pygame.mixer.Sound.play(sound)
                item.move_random()
                self.snake.grow()

        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "GAME OVER"

        self.render_background()
        self.display_score()
        self.snake.move()
        self.itemManager.draw_all()

        pygame.display.update()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + BLOCK_SIZE:
            if y1 >= y2 and y1 < y2 + BLOCK_SIZE:
                return True

    def run(self):
        while self.running:
            self.menu.show()
            
            while self.playing:
                self.check_events()
                try:
                    self.game_Logic() 
                except Exception as e:
                    self.game_over()
                time.sleep(0.125)


    def game_over(self):
        self.stop_background_music()
        sound = pygame.mixer.Sound("resources/gameover.mp3")
        pygame.mixer.Sound.play(sound)
        self.playing = False
        self.state = "GAMEOVER"
        print(self.player_name)

    def init_start(self):
        self.play_background_music()
        self.snake = Snake(self.screen)
        self.snake.draw()
        self.itemManager = ItemManager(self)


    def display_score(self):
        font = pygame.font.SysFont(self.font_name, 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 200, 200))
        self.screen.blit(score, (SCREEN_WIDTH-100,10))

    def play_background_music(self):
        print("play music")
        #pygame.mixer.music.load("resources/sound.mp3")
        #pygame.mixer.music.play()

    def stop_background_music(self):
        print("stop music")
        #pygame.mixer.music.stop()

    def check_events(self, input_box=None):
        for event in pygame.event.get():
            if self.state == "ENTERNAME":
                input_box.handle_event(event)
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.playing = False
                    self.state = "MENU"
                if event.key == K_RETURN:
                    self.playing = True
                    self.state = "PLAY"
                if event.key == K_UP:
                    self.snake.move_direction_check("UP")
                if event.key == K_DOWN:
                    self.snake.move_direction_check("DOWN")
                if event.key == K_LEFT:
                    self.snake.move_direction_check("LEFT")
                if event.key == K_RIGHT:
                    self.snake.move_direction_check("RIGHT")
            elif event.type == QUIT:
                self.state = "QUIT"
                self.running = False
                self.playing = False
                pygame.quit()
            
            
