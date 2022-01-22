import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


game_is_on = True
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


def quit_game():
    global game_is_on
    game_is_on = False


screen.onkey(quit_game, "q")
screen.onkey(player.move, "Up")
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # My solution
    # if len(car_manager.cars) < 30:
    #     car_manager.generate_car()

    # Her solution
    if counter == 0:
        car_manager.generate_car()

    car_manager.move_cars()

    # Detect collision
    for car in car_manager.cars:
        if abs(player.ycor() - car.ycor()) <= 22.5 and player.distance(car) <= 22.5:
            game_is_on = False
            scoreboard.game_over()

    # Level Completed!
    if player.ycor() == FINISH_LINE_Y:
        scoreboard.level_completed()
        car_manager.level_completed()
        player.restart()

    # car_manager.restart_cars()
    counter += 1
    if counter > 5:
        counter = 0


screen.exitonclick()
