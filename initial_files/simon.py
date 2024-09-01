from turtle import Turtle


class Simon(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.setposition(position)

    def move(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def replay(self):
        self.setposition((0, -280))
