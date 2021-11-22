import arcade
from constants import *
from time import sleep

class Paddle():
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

    def paddle_Ax(self):
        return self.pong_Ax
        

    def paddle_Ay(self):
        return self.pong_Ay
        

    def paddle_Bx(self):
        return self.pong_Bx

    def paddle_By(self):
        return self.pong_By
    

