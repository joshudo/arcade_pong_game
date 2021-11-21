from game.window import MyGameWindow
import arcade

def main():
    MyGameWindow(1280, 720, "Ping Pong")
    arcade.run()

if __name__ == "__main__":
    main()