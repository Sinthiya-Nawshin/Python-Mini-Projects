import random
from turtle import Turtle, Screen

is_race_on = False

screen = Screen()
screen.setup(520, 400)
user_input = screen.textinput("Make your bet", "Which turtle do you want to choose? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "orange", "magenta"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_input:
                print(f"You've won! The {wining_color} is the winner.")
            else:
                print(f"You've lost! The {wining_color} is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
