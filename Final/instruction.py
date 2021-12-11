import arcade
from main_game import MyWindow

class InstructionView(arcade.View):
      

    def on_show(self):
        # Create a surface we can draw on
        arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
        

    def on_draw(self):
        
        """Draw all the instruction about the game """
        
        arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)
        arcade.start_render()
        arcade.draw_text("Instructions",  self.window.width / 2, self.window.height / 1.5,
                         arcade.color.WHITE, bold=True, font_size=50,anchor_x="center")
        arcade.draw_text('Left player controls: "W" to move paddle up. "S" to move paddle down', self.window.width / 2, self.window.height / 2-15,
                         arcade.color.WHITE, bold=True,font_size=11, anchor_x="center")
        arcade.draw_text('Right player controls: "Up arrow" to move paddle up. "Down arrow" to move paddle down', self.window.width / 2, self.window.height / 2-30,
                         arcade.color.WHITE, bold=True, font_size=11, anchor_x="center")
        arcade.draw_text('Press "P" to pause & continue the game, "Q" to immediately quit the game', self.window.width / 2, self.window.height / 2-75,
                         arcade.color.WHITE, bold=True,font_size=11, anchor_x="center")
        arcade.draw_text("First player to 10 points wins!", self.window.width / 2, self.window.height / 2-110,
                         arcade.color.WHITE, bold=True, font_size=15, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-220,
                         arcade.color.WHITE, italic=True,font_size=20, anchor_x="center")
                         
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        
        """ Handle Mouse Motion """
        
        game_view = MyWindow()
        self.window.show_view(game_view)