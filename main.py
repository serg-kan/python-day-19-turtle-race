from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

screen = Screen()
screen.setup(width=500, height=400)

starting_position_x = -230
starting_position_y = -100

bet_turtle = screen.textinput(title="Make a bet", prompt="Enter the color")

for i in range(0, len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(starting_position_x, starting_position_y)

    starting_position_y += 30

    turtles.append({
        "name": colors[i],
        "turtle": new_turtle,
        "position_x": -230
    })

is_winner = False
current_winner_position_x = -230

# while not is_winner:
while not is_winner:
    for i in range(0, len(turtles)):
        step = random.randint(5, 20)
        turtles[i]["position_x"] += step
        turtles[i]["turtle"].forward(step)

        if turtles[i]["position_x"] >= 230:
            is_winner = True
            winner = turtles[i]
            break

if winner["name"] == bet_turtle:
    print("You win")
else:
    print(f'You lose. Winner is {winner["name"]}')



screen.exitonclick()
