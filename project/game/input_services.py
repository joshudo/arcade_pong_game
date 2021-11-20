import arcade
from paddle import Paddle

class InputService:

    def __init__(self):
        pass

    def on_key_press(self, key):
        if key == Paddle.UP:
            print("I chose to go up")
        if key == Paddle.DOWN:
            print("I chose to go down")


