# from arcade.key import LEFT
# from paddle import Paddle
import arcade 

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.MSU_GREEN)

        self.c_x = 100
        self.c_y = 100
        self.x_speed = 300
        self.y_speed = 150
        self.player1_y = 360
        self.player1_speed = 250
        self.player2_y = 360
        self.player2_speed = 250
        self.player1_up = False
        self.player1_down = False
        self.player2_up = False
        self.player2_down = False
        

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lines([(640,0), (640,720)], arcade.color.BLACK, 4,)
        arcade.draw_circle_filled(self.c_x,self.c_y,15, arcade.color.WHITE_SMOKE, 30)
        arcade.draw_rectangle_filled(10, self.player1_y,20,100, arcade.color.RED, )
        arcade.draw_rectangle_filled(1270, self.player2_y,20,100, arcade.color.BLUE, )
    
    def on_update(self, delta_time):
        self.c_x += self.x_speed * delta_time
        self.c_y += self.y_speed * delta_time

        if self.c_x > 1280 -15 or self.c_x < 0 + 15:
            self.x_speed *= -1
        if self.c_y > 720 - 15 or self.c_x < 0 + 15:
            self.y_speed *= -1
        if self.player1_up:
            self.player1_y += self.player1_speed * delta_time
        if self.player1_down:
            self.player1_y -= self.player1_speed * delta_time
        
        if self.player2_up:
            self.player2_y += self.player2_speed * delta_time
        if self.player2_down:
            self.player2_y -= self.player2_speed * delta_time
   
    def on_key_press(self, symbol, modifier):
  
        # Checking the button pressed
        # is up arrow key or not
        if symbol == arcade.key.W:
            self.player1_up = True
        elif symbol == arcade.key.S:
            self.player1_down = True
        elif symbol == arcade.key.UP:
            self.player2_up = True
        elif symbol == arcade.key.DOWN:
            self.player2_down = True
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.W:
            self.player1_up = False
        elif symbol == arcade.key.S:
            self.player1_down = False
        elif symbol == arcade.key.UP:
            self.player2_up = False
        elif symbol == arcade.key.DOWN:
            self.player2_down = False
        
        





    


