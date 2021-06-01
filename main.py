import time
from turtle import Screen
from player import FINISH_LINE_Y, Player, STARTING_POSITION
from car_manager import CarManager, MOVE_INCREMENT, STARTING_MOVE_DISTANCE
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()
screen.onkey(player.player_move, "Up")

game_is_on = True
increment = 0


while game_is_on:
    time.sleep(0.1)
    screen.update()    
    carmanager.add_car()    
    carmanager.car_move(STARTING_MOVE_DISTANCE)

    #Detect collision between turtle and cars
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Detect when turtle reaches finish line
    if player.ycor() == FINISH_LINE_Y:
        increment += 1
        scoreboard.reset_score()
        player.setposition(STARTING_POSITION)
        carmanager.car_move(STARTING_MOVE_DISTANCE + (increment*MOVE_INCREMENT))

screen.exitonclick()

    