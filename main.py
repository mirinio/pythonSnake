import pygame
import time 
from pygame.locals import *

from snake import Snake
from Apple import Apple
from settings import *

from snake2 import irgendöbis

class Game:
    def __init__(self):
        pygame.init() 
        pygame.mixer.init()
        self.play_background_music()
        self.surface = pygame.display.set_mode((1920, 1080)) 
        self.surface.fill(BACKGROUND_COLOR)
        pygame.display.flip()
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.running = True
  


    def render_background(self):
        bg = pygame.image.load("resources/space.jpg")
        self.surface.blit(bg, (0,0))

    def draw(self):
        
        self.snake.move()
        self.apple.draw()

    def play_background_music(self):
        print("hi")
        #pygame.mixer.music.load("resources/bgmusig.mp3")
        #pygame.mixer.music.play()

    def play(self):
        self.render_background()
        self.draw()
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            #sound = pygame.mixer.Sound("resources/ding.mp3")
            #pygame.mixer.Sound.play(sound)
            self.apple.move_random()
            self.snake.grow()

        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "GAME OVER"

        self.display_score()
        pygame.display.flip()
        
    def run(self):
        pause = False

        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                    if event.key == K_RETURN:
                        pause = False
                    if event.key == K_UP:
                        self.snake.move_direction = "UP"
                    if event.key == K_DOWN:
                        self.snake.move_direction = "DOWN"
                    if event.key == K_LEFT:
                        self.snake.move_direction = "LEFT"
                    if event.key == K_RIGHT:
                        self.snake.move_direction = "RIGHT"
                elif event.type == QUIT:
                    self.running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.game_over()
                pause = True
                self.reset()
            time.sleep(0.00001)

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def game_over(self):
        self.render_background()
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)
        game_over_txt = font.render(f"GAME OVER", True, (255, 255, 255))
        self.surface.blit(game_over_txt, (800, 500))
        score_txt = font.render(f"SCORE {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score_txt, (800, 550))
        again_txt = font.render("To play again press Enter. To exit press Escape", True, (255, 255, 255))
        self.surface.blit(again_txt, (800,600))
        pygame.display.flip()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + BLOCK_SIZE:
            if y1 >= y2 and y1 < y2 + BLOCK_SIZE:
                return True


    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 200, 200))
        self.surface.blit(score, (1800,10))


if __name__ == "__main__":
    
    game = Game()
    game.run()