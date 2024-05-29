from turtle import Turtle, Screen

timmy = Turtle()

def forward():
    timmy.forward(10)

def backward():
    timmy.back(10)

def turn_left():
    timmy.left(5)

def turn_right():
    timmy.right(5)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    
screen = Screen()
screen.listen()

while screen.onkeypress(fun=forward, key='w'):
    screen.onkey(fun=forward, key='w')

while screen.onkeypress(fun=backward, key='s'):
    screen.onkey(fun=backward, key='s')

while screen.onkeypress(fun=turn_left,key='a'):
    screen.onkey(fun=turn_left, key='a')

while screen.onkeypress(fun=turn_right,key='d'):
    screen.onkey(fun=turn_right, key='d')

screen.onkey(fun=clear, key='c')

screen.exitonclick()