import arcade
import sys
from time import sleep

from arcade.window_commands import pause
from ball import Ball
from paddle import Paddle
from constants import *
import os
import PIL.Image

path1 = "Final/platform.png"
path2 = "Final/ball1.png"
path3 = "Final/p1.png"
path4 = "Final/p2.jpg"

class InstructionView(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        

    def on_draw(self):
        arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)
        arcade.start_render()
        arcade.draw_text("Instructions",  self.window.width / 2, self.window.height / 1.5,
                         arcade.color.WHITE, bold=True, font_size=50,anchor_x="center")
        arcade.draw_text('Left player controls: "W" to move paddle up. "S" to move paddle down', self.window.width / 2, self.window.height / 2-15,
                         arcade.color.WHITE, bold=True,font_size=11, anchor_x="center")
        arcade.draw_text('Right player controls: "Up arrow" to move paddle up. "Down arrow" to move paddle down', self.window.width / 2, self.window.height / 2-30,
                         arcade.color.WHITE, bold=True, font_size=11, anchor_x="center")
        arcade.draw_text("First player to 10 points wins!", self.window.width / 2, self.window.height / 2-110,
                         arcade.color.WHITE, bold=True, font_size=15, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-220,
                         arcade.color.WHITE, italic=True,font_size=20, anchor_x="center")
                         
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = Window()
        self.window.show_view(game_view)


class Window(arcade.View):
    def __init__(self):
        super().__init__()
        self.collision_sound = arcade.load_sound('Final/bounce.wav')
        self.pong_A_score = 0
        self.pong_B_score = 0
        self.ball = Ball()
        self.paddle = Paddle()
        self.total_time = 180.0

        self.pong_sprite_A = arcade.Sprite(path1)
        self.pong_Ax = self.paddle.paddle_Ax()
        self.pong_Ay = self.paddle.paddle_Ay()
        self.pongA_change = 0
        
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
        arcade.set_background_color(arcade.color.BLACK)
        arcade.start_render()

        arcade.draw_text(f' Player 1: {self.pong_A_score} | Player 2: {self.pong_B_score}', 241, SCREEN_HEIGHT-30, arcade.csscolor.WHITE, 14)
        arcade.draw_line(350, 500, 350, 0, arcade.color.WHITE, 2.5)

        #setup for the countdown timer
        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        output = f"Time: {minutes:02d}:{seconds:02d}"
        arcade.draw_text(output,SCREEN_WIDTH/5,470,arcade.color.WHITE,12)

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
        
        self.total_time -= delta_time

        if arcade.check_for_collision(self.ball_sprite, self.pong_sprite_A):
            self.ball_change_x = +1
            arcade.play_sound(self.collision_sound, volume=0.5)
            
        elif arcade.check_for_collision(self.ball_sprite, self.pong_sprite_B):
            self.ball_change_x = -1
            arcade.play_sound(self.collision_sound, volume=0.5)
      
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
            arcade.play_sound(self.collision_sound, volume=0.5)

        if self.ball_position_x > SCREEN_WIDTH - 10:
           self.pong_A_score += 1
           sleep(1)
           self.ball_position_x = SCREEN_WIDTH / 2
           self.ball_position_y = SCREEN_HEIGHT / 2
           self.ball_change_x *= -1
           arcade.play_sound(self.collision_sound, volume=0.5)

        if self.ball_position_y < 10 or self.ball_position_y > SCREEN_HEIGHT - 10:
            self.ball_change_y *= -1
            arcade.play_sound(self.collision_sound, volume=0.5)

        if self.pong_A_score == 10:
            arcade.start_render()
            self.background = arcade.load_texture(path3)
            arcade.draw_texture_rectangle(350, SCREEN_HEIGHT-160, 200, 200, self.background)
            arcade.finish_render()
            arcade.play_sound(self.collision_sound, volume= 0)

        if self.pong_B_score == 10:
            arcade.start_render()
            self.background2 = arcade.load_texture(path4)
            arcade.draw_texture_rectangle(350, SCREEN_HEIGHT-160, 200, 200, self.background2)
            arcade.finish_render()
            arcade.play_sound(self.collision_sound, volume= 0)
        if self.total_time <= 0:
            if self.pong_A_score > self.pong_B_score:
                arcade.start_render()
                self.background = arcade.load_texture(path3)
                arcade.draw_texture_rectangle(350, SCREEN_HEIGHT-160, 200, 200, self.background)
                arcade.finish_render()
                arcade.play_sound(self.collision_sound, volume= 0)
            elif self.pong_B_score > self.pong_A_score:
                arcade.start_render()
                self.background2 = arcade.load_texture(path4)
                arcade.draw_texture_rectangle(350, SCREEN_HEIGHT-160, 200, 200, self.background2)
                arcade.finish_render()
                arcade.play_sound(self.collision_sound, volume= 0)
            else:
                pass



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