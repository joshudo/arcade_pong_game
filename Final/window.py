import arcade
import sys
from time import sleep

from arcade.window_commands import pause
from ball import Ball
from paths import *
from paddle import Paddle
from constants import *
import os
import PIL.Image

path1 = "Final/platform.png"
path2 = "Final/ball1.png"
path3 = "Final/p1.png"
path4 = "Final/p2.jpg"


class Window(arcade.View):
    def __init__(self):
        
        """ Game Initializer """
        # Call the parent class (Sprite) Initializer        
        super().__init__()
        self.collision_sound = arcade.load_sound(path5)
        self.pong_A_score = 0
        self.pong_B_score = 0
        self.ball = Ball()
        self.paddle = Paddle()
        self.total_time = 180.0
        self.paused = False

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
        
        """ Draw everything """
        
        #Set the background color of the screen
        arcade.set_background_color(arcade.color.BLACK)
        arcade.start_render()
        # Print the score
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

    # Update the position of the ball
    def update(self, delta_time: float):
        
        """ Movement and game logic that updates all game objects """
        
        if self.paused:
            return
        
        self.total_time -= delta_time

        #Check collisions bewtween main Sprites
        if arcade.check_for_collision(self.ball_sprite, self.pong_sprite_A):
            self.ball_change_x = +1
            arcade.play_sound(self.collision_sound, volume=0.5)
            
        elif arcade.check_for_collision(self.ball_sprite, self.pong_sprite_B):
            self.ball_change_x = -1
            arcade.play_sound(self.collision_sound, volume=0.5)
      
        self.pong_Ay += self.pongA_change
        self.pong_By += self.pongB_change
        
        #Changing position of the ball according to coordinates
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

        #Condition to check which player or pong wins when reaching a score of 10
        if self.pong_A_score == 10:
            arcade.start_render()
            self.background = arcade.load_texture(path3)
            # Get a rectangle object and get the height of the screen
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
        #Keyboard binding
        
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/unpause the game
        W/S: Move Up, Down
        Arrows: Move Up, Down
        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        
        if symbol == arcade.key.P:
            self.paused = not self.paused
        if symbol == arcade.key.Q:
            arcade.close_window()
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
    #set key controls to hit the ball
    def on_key_release(self, symbol: int, modifiers: int):
        
        """Undo movement vectors when movement keys are released
        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.pongA_change = 0
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.pongB_change = 0