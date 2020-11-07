import copy as cp
import random


# Consider using the modules imported above.

class Hat:
    contents = []

    def __init__(self, **kwargs):
        print(f"'QWERTY'{kwargs}")
        for ball in kwargs.items():
            key, val = ball
            # print(ball)
            for i in range(val):
                self.contents.append(key)
        print(f"'QWERTY'{self.contents}")

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
