from turtle import Turtle

import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("blue")
        self.shapesize(stretch_len=0.9,stretch_wid=0.9)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
