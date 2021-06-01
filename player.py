from turtle import Turtle
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    #Create turtle player
    def __init__(self):
        super().__init__(shape="turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.setposition(0,-280)


    def player_move(self):
        self.forward(MOVE_DISTANCE)

