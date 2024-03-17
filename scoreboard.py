from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.penup()
        self.color("white")
        self.score = 0
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"score: {self.score}", align="center", font=('Arial', 8, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"game over", align="center", font=('Arial', 8, 'normal'))
