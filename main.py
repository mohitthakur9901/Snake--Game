from turtle import Turtle, Screen
START_POSITION=[(0,0),(-5,0),(-10,0)]
MOVE_FORWORD=20
screen=Screen()
screen.listen()
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake():
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]
    def create_snake(self):
        for postion in START_POSITION:
            self.add_segment(postion)

    def add_segment(self,postion):
        snake_1 = Turtle(shape="circle")
        snake_1.penup()
        snake_1.color("white")
        snake_1.goto(postion)
        self.segment.append(snake_1)

    def extend_snake(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
            for seg_num in range(len(self.segment) - 1, 0, -1):
                new_x = self.segment[seg_num - 1].xcor()
                new_y = self.segment[seg_num - 1].ycor()
                self.segment[seg_num].goto(new_x, new_y)
            self.head.forward(MOVE_FORWORD)
    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP).upper()
    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN).upper()
    def left(self):
        if self.head.heading != LEFT:
            self.head.setheading(LEFT).upper()
    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT).upper()



