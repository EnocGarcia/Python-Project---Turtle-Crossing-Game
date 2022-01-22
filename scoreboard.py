from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.goto(x=-275, y=250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)

    def level_completed(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.home()
        self.write("GAME OVER", False, "center", FONT)
