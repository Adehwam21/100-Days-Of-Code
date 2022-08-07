import turtle
import random
import time

canvas = turtle.getscreen()
turtle.bgcolor("black")
p1 = turtle.Turtle()
p2 = turtle.Turtle()
finish_line = turtle.Turtle()
def canvas_setup():
    finish_line.penup()
    finish_line.shape("circle")
    finish_line.pensize(7)
    finish_line.goto(-270, 200)
    finish_line.forward(540)
    finish_line.rt(90)
    finish_line.pendown()
    finish_line.color("white")
    finish_line.forward(270)

    p1.penup()
    p1.shape("turtle")
    p1.pensize(10)
    p1.fillcolor("red")
    p1.goto(-270, 30)
    p1.pendown()

    p2.penup()
    p2.shape("turtle")
    p2.pensize(10)
    p2.fillcolor("blue")
    p2.goto(-270, 100)
    p2.pendown()

def function():
    pace = [1, 2, 3, 4, 5, 6]
    moves = 1
    finish1 = 0
    finish2 = 0

    input("Press enter to start the race: ")
    while moves <= 20:
        print(f"Move : {moves}")
        input("Red's turn. Press enter to run: ")
        outcome1 = random.choice(pace)
        distance1 = outcome1 * 15
        print(f"You got a {outcome1}, so you'll move {distance1} steps")
        p1.penup()
        p1.fd(distance1)
        finish1 += distance1

        input("Blue's turn. Press enter to run: ")
        outcome2 = random.choice(pace)
        distance2 = outcome2 * 15
        print(f"You got a {outcome2}, so you'll move {distance2} steps")
        p2.penup()
        p2.fd(distance2)
        finish2 += distance2

        moves += 1
        print()
        if finish1 >= 540:
            print("Red wins")
            break
        elif finish2 >= 540:
            print("Blue wins")
            break
        elif moves > 20:
            print("Time up! out of moves")
            break


canvas_setup()
function()

time.sleep(20)
