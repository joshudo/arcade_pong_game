import arcade
import sys
from time import sleep
from ball import Ball
from paddle import Paddle
from constants import *


path1 = "platform.png"
path2 = "ball1.png"


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'PONG', update_rate=0.008)

        self.pong_A_score = 0
        self.pong_B_score = 0
        self.ball = Ball()
        self.paddle = Paddle()

        """self.pong_sprite_A = arcade.Sprite(path1)
        self.pong_Ax = self.paddle.pong_Ax
        self.pong_Ay = self.paddle.pong_Ay
        self.pongA_change = 0"""
        self.pong_sprite_A = arcade.Sprite(path1)
        self.pong_Ax = self.paddle.paddle_Ax()
        self.pong_Ay = self.paddle.paddle_Ay()
        self.pongA_change = 0
        


        """self.pong_sprite_B = arcade.Sprite(path1)
        self.pong_Bx = self.paddle.pong_Bx
        self.pong_By = self.paddle.pong_By
        self.pongB_change = 0"""
        self.pong_sprite_B = arcade.Sprite(path1)
        self.pong_Bx = self.paddle.paddle_Bx()
        self.pong_By = self.paddle.paddle_By()
        self.pongB_change = 0



        self.ball_sprite = arcade.Sprite(path2)
        self.ball_position_x  = self.ball.position_x
        self.ball_position_y = self.ball.position_y
        self.ball_change_x = self.ball.change_x
        self.ball_change_y = self.ball.change_y

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(f' Player 1: {self.pong_A_score} | Player 2: {self.pong_B_score}', SCREEN_WIDTH/2, SCREEN_HEIGHT-30, arcade.csscolor.WHITE, 14)

        
        self.pong_sprite_A.center_x = self.pong_Ax
        self.pong_sprite_A.center_y = self.pong_Ay
        self.pong_sprite_A.draw()

        self.pong_sprite_B.center_x = self.pong_Bx
        self.pong_sprite_B.center_y = self.pong_By
        self.pong_sprite_B.draw()

        self.ball_sprite.center_x = self.ball_position_x
        self.ball_sprite.center_y = self.ball_position_y
        self.ball_sprite.draw()

    def update(self, delta_time: float):
        
        if arcade.check_for_collision(self.ball_sprite, self.pong_sprite_A):
            self.ball_change_x = +1
            
        elif arcade.check_for_collision(self.ball_sprite, self.pong_sprite_B):
            self.ball_change_x = -1
      
        self.pong_Ay += self.pongA_change
        self.pong_By += self.pongB_change
        

        self.ball_position_x += self.ball_change_x
        self.ball_position_y += self.ball_change_y

        if self.ball_position_x < 10:
            self.pong_B_score += 1
            sleep(1)
            self.ball_position_x = SCREEN_WIDTH / 2
            self.ball_position_y = SCREEN_HEIGHT / 2
            self.ball_change_x *= -1

        if self.ball_position_x > SCREEN_WIDTH - 10:
           self.pong_A_score += 1
           sleep(1)
           self.ball_position_x = SCREEN_WIDTH / 2
           self.ball_position_y = SCREEN_HEIGHT / 2
           self.ball_change_x *= -1

        if self.ball_position_y < 10 or self.ball_position_y > SCREEN_HEIGHT - 10:
            self.ball_change_y *= -1

        

        if self.pong_Ay < 50:
            self.pong_Ay += SCROLLING_SPEED
        if self.pong_Ay > SCREEN_HEIGHT-50:
            self.pong_Ay -= SCROLLING_SPEED
        if self.pong_By < 50:
            self.pong_By += SCROLLING_SPEED
        if self.pong_By > SCREEN_HEIGHT-50:
            self.pong_By -= SCROLLING_SPEED



    def on_key_press(self, symbol: int, modifiers: int):
        
        if symbol == arcade.key.W:
            self.pongA_change = SCROLLING_SPEED
        if symbol == arcade.key.S:
            self.pongA_change = -SCROLLING_SPEED
        if symbol == arcade.key.UP:
            self.pongB_change = SCROLLING_SPEED
        if symbol == arcade.key.DOWN:
            self.pongB_change = -SCROLLING_SPEED
        """if symbol == arcade.key.Q:
            user = input("Do you want to exit the game?")
            if user == 'Y' or user == 'y':
                print("Thanks for playing")
            sys.exit()"""

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.pongA_change = 0
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.pongB_change = 0




"""def main():
    win = MyWindow()
    arcade.run()

if __name__ == '__main__':
    main()"""