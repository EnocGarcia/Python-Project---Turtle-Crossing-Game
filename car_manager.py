from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.setheading(180)
        self.car_speed = 0
        self.y_pos = randint(-250, 250)
        self.x_pos = randint(300, 600)
        self.starting_position = (self.x_pos, self.y_pos)
        self.goto(self.starting_position)

    def move(self):
        self.forward(self.car_speed)


class CarManager:
    def __init__(self):
        self.reset_position = -320
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def generate_car(self):
        car = Car()
        car.car_speed = self.car_speed
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move()

    def level_completed(self):
        self.car_speed += MOVE_INCREMENT
        for car in self.cars:
            car.car_speed = self.car_speed

    def restart_cars(self):
        for car in self.cars:
            if car.xcor() <= self.reset_position:
                car.goto(car.starting_position)


