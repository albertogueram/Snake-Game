from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as score:
            self.highscore = int(score.read())
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | Highscore: {self.highscore}", align="center", font=('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("score.txt", "w") as score:
                score.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def refresh(self):
        self.score += 1
        self.update_scoreboard()




