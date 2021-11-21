from game.window import MyGameWindow
import arcade
import os

def main():
    MyGameWindow(1280, 720, "Ping Pong")
    arcade.load_sound('project/bounce.wav')
    arcade.run()

if __name__ == "__main__":
    main()