import arcade
from constants import *
from time import sleep


# This class represents the ball
class Ball():
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = SCREEN_WIDTH / 2
        self.position_y = SCREEN_HEIGHT / 2
        # Change the position (x and y) according to the speed and direction
        self.change_x = BALL_SPEED
        self.change_y = BALL_SPEED

    def position_x(self):
        return SCREEN_WIDTH / 2

    def position_y(self):
        return SCREEN_HEIGHT / 2

    def change_x(self):
        return BALL_SPEED

    def change_y(self):
        return BALL_SPEED
        
      

    