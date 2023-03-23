from turtle import Turtle, Screen
import random
is_race_on = False
my_Screen = Screen()
my_Screen.setup(width=500, height=400)
my_Screen.listen()
user_bat = my_Screen.textinput(title="User bat ",
                               prompt="Which turtle will win?Enter the color name")

y_position = [-70, -40, -10, 20, 50, 80]
color = ["blue", "orange", "Brown", "green", "red", "magenta"]
all_turtle = []

for rang in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(color[rang])
    t.goto(x=-230, y=y_position[rang])
    all_turtle.append(t)

if user_bat:
    is_race_on = True
    while is_race_on:
        for turtle in all_turtle:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bat.lower():
                    print("Your Turtle win the Race 🤘")
                else:
                    print("Your Turtle Loose the Race🤯")
                is_race_on = False
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


my_Screen.exitonclick()
