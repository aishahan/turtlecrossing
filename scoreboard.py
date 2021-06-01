from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.setposition(-270, 270)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align = "left", font = FONT)

    def reset_score(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align = "center", font = FONT)        