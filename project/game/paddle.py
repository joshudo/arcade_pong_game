import arcade

class Paddle:

    def __init__(self, paddle_side):
        if paddle_side == "left":
            self.UP = arcade.key.W
            self.DOWN = arcade.key.S
        elif paddle_side == "right":
            self.UP = arcade.key.UP
            self.DOWN = arcade.key.DOWN


        


        


    