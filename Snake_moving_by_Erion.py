    
    def snake_moving_settings(self):
           self.x=SNAKE_MOVING_SPEED
           self.y=0
           self.roadmap=[(0,0)]
           self.bodylength=3
           self.snake_food=None
           self.gamevalid=1
           self.score=0
           return
    
    def snake_head_moving(self, event=None):
           key=event.keysym
           if key=='Left':
                  self.turn_left()
           elif key=='Right':
                  self.turn_right()
           elif key=='Up':
                  self.turn_up()
           elif key=='Down':
                  self.turn_down()
           else:
                  pass
           return
    
    def turn_left(self):
           self.x=-SNAKE_MOVING_SPEED
           self.y=0
           return

    def turn_right(self):
           self.x=SNAKE_MOVING_SPEED
           self.y=0
           return

    def turn_up(self):
           self.x=0
           self.y=-SNAKE_MOVING_SPEED
           return

    def turn_down(self):
           self.x=0
           self.y=SNAKE_MOVING_SPEED
           return