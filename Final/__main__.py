<<<<<<< HEAD
from main_game import *
from instruction import InstructionView
=======
from window import *
>>>>>>> 34b7843a9fbdfff1bdb95cfa8c5002db87891512
import arcade
from constants import *

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, update_rate=0.008, )
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()

if __name__ == '__main__':
    main()