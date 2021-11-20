from arcade.key import LEFT
import arcade 

class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.ASH_GREY)

        self.c_x = 100
        self.c_y = 100
        self.x_speed = 300
        self.y_speed = 150

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lines([(640,0), (640,720)], arcade.color.BLACK, 4,)
        arcade.draw_circle_filled(self.c_x,self.c_y,15, arcade.color.RED, 30)
    
    def on_update(self, delta_time):
        self.c_x += self.x_speed * delta_time
        self.c_y += self.y_speed * delta_time

        if self.c_x > 1280 -15 or self.c_x < 0 + 15:
            self.x_speed *= -1
        if self.c_y > 720 - 15 or self.c_x < 0 + 15:
            self.y_speed *= -1
   
    def on_key_press(self, symbol, modifier):
  
        # Checking the button pressed
        # is up arrow key or not
        if symbol == arcade.key.UP:
            print("Right player upper key has been pressed")
        elif symbol == arcade.key.DOWN:
            print("Right player down key has been pressed")
        elif symbol == arcade.key.W:
            print("Left player up key has been pressed")
        elif symbol == arcade.key.S:
            print("Left player down key has been pressed")
        





    


