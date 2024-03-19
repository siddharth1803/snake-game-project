from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.penup()
        self.color("white")
        self.score = 0
        with open("high_score_file") as data:
            self.high_score = int(data.read())

        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score} high score: {self.high_score}", align="center",
                   font=('Arial', 8, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def save_high_score(self):
        with open("high_score_file", mode="w") as score_file:
            score_file.write(str(self.high_score))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

        self.score = 0
        self.update_score()
