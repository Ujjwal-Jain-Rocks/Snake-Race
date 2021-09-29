from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white", "white")
        self.draw()
        with open("high_score.txt") as f:
            self.high_score = int(f.read())

    def update(self):
        self.score += 1
        self.clear()
        self.draw()

    def draw(self):
        self.goto(0, 270)
        self.write(f"Score :- {self.score} High Score: {self.high_score}", False, "center", ("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.draw()
