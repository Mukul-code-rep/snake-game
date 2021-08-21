import turtle as t

ALIGN = 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.scoreboard_update()

    def scoreboard_update(self):
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.reset_score()
        self.scoreboard_update()

    def reset_score(self):
        if self.high_score < self.score:
            self.high_score = self.score

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGN, font=FONT)
        with open('data.txt', mode='r') as file:
            content = file.read()
        with open('data.txt', mode='w') as file:
            if int(content) < self.high_score:
                file.write(str(self.high_score))
            else:
                file.write(content)
