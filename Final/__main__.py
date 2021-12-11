from instruction import *
import arcade
from constants import *

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, update_rate=0.008, )
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()

if __name__ == '__main__':
    main()