from turtle import Turtle, Screen
from simon import Simon
from car import CarManager
from scoreboard import Scoreboard
import time
import random


def start_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.title('Turtle Race')

    # Initialize the game
    game_on = True
    simon = Simon((0, -280))
    cars = CarManager()
    scoreboard = Scoreboard()

    # Restart the game
    def on_escape():
        nonlocal game_on  # Access the global game_on variable
        game_on = False
        screen.clearscreen()
        start_game()

    # Set up key bindings
    screen.onkeypress(simon.move, 'Up')
    screen.onkey(on_escape, 'Escape')
    screen.listen()

    # Main game loop
    while game_on:
        time.sleep(0.1)
        screen.update()
        cars.create_car()
        cars.move_cars()

        # Detect when turtle passes the success line
        if simon.ycor() > 300:
            simon.replay()
            scoreboard.point()
            cars.accelerate()

        # Detect collistion between car and turtle
        for car in cars.all_cars:
            if simon.distance(car) < 20 and simon.ycor() < car.ycor():
                game_on = False
                scoreboard.game_over()

    screen.exitonclick()


start_game()
