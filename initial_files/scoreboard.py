from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(x=-150, y=240)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.score}', align='center', font=('Courier', 20, 'normal'))

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setposition(x=0, y=0)
        self.write('GAME OVER!', align='center', font=('Courier', 20, 'normal'))
