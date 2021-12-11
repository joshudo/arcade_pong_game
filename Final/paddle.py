import arcade
from constants import *
from time import sleep

# This class represents the bars or paddle on the sides of the screen that the players control
class Paddle():
    # Constructor function
    def __init__(self):
        self.pong_A_change = 0
        self.pong_B_change = 0
        self.pong_Ax = 40
        self.pong_Ay = SCREEN_HEIGHT/2
        self.pong_Bx = SCREEN_WIDTH-40
        self.pong_By = SCREEN_HEIGHT/2
        
    def paddleA_change(self):
        return self.pong_A_change

    def paddleB_change(self):
        return self.pong_B_change

   #Direction of paddle A
    def paddle_Ax(self):
        return self.pong_Ax
        

    def paddle_Ay(self):
        return self.pong_Ay
        
    #Direction of paddle B
    def paddle_Bx(self):
        return self.pong_Bx

    def paddle_By(self):
        return self.pong_By
    

