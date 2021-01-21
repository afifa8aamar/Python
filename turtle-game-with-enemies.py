import turtle

win = turtle.Screen()
win.bgcolor("Black")
win.title("leqcia5")
win.setup(600,600)


shape_one = turtle.Turtle()
shape_one.color("white")
shape_one.shape("triangle")
#shape_one.shapesize(1,1)
shape_one.penup()
shape_one.speed(0)
shape_one.setposition(-200,-200)
shape_one.pendown()
shape_one.pensize(2)
for side in range(4):
    shape_one.fd(400)
    shape_one.lt(90)

shape_one.hideturtle()

shape_two = turtle.Turtle()
shape_two.color("white")
shape_two.shape("triangle")
shape_two.shapesize(1.5,1.5)
shape_two.penup()
shape_two.speed(0)
shape_two.setposition(0,-180)
shape_two.lt(90)
#shape_two.pendown()


shape_three = turtle.Turtle()
shape_three.color("red")
shape_three.shape("circle")
shape_three.shapesize(2,2)
shape_three.penup()
shape_three.speed(0)
shape_three.setposition(0,170)
#shape_three.lt(90)




def move_right():
    x = shape_two.xcor()
    x=x+10
    if x>=180:
        x=180
    shape_two.setx(x)


def move_left():
    x = shape_two.xcor()
    x=x-10
    if x<=-180:
        x=-180
    shape_two.setx(x)

def move_up():
    y=shape_two.ycor()
    y=y+10
    if y>=180:
        y=180
    shape_two.sety(y)


def move_down():
    y=shape_two.ycor()
    y=y-10
    if y<=-180:
        y=-180
    shape_two.sety(y)


turtle.listen()
turtle.onkey(move_right,"Right")
turtle.onkey(move_left,"Left")
turtle.onkey(move_up,"Up")
turtle.onkey(move_down,"Down")

enemyspeed=5
while True:

    x=shape_three.xcor()
    y=shape_three.ycor()

    x=x+enemyspeed
    if x>=180:
        enemyspeed=enemyspeed*-1
        y=y-10
    if x<=-180:
        enemyspeed=enemyspeed*-1
        y=y-10
        
    
    shape_three.setx(x)
    shape_three.sety(y)
 








-----------------------------------------------------------------------------------------------







import turtle

win = turtle.Screen()
win.bgcolor("Black")
win.title("leqcia5")
win.setup(600,600)


shape_one = turtle.Turtle()
shape_one.color("white")
shape_one.shape("triangle")
#shape_one.shapesize(1,1)
shape_one.penup()
shape_one.speed(0)
shape_one.setposition(-200,-200)
shape_one.pendown()
shape_one.pensize(2)
for side in range(4):
    shape_one.fd(400)
    shape_one.lt(90)

shape_one.hideturtle()

shape_two = turtle.Turtle()
shape_two.color("white")
shape_two.shape("triangle")
shape_two.shapesize(1.5,1.5)
shape_two.penup()
shape_two.speed(0)
shape_two.setposition(0,-180)
shape_two.lt(90)
#shape_two.pendown()


shape_three = turtle.Turtle()
shape_three.color("red")
shape_three.shape("circle")
shape_three.shapesize(2,2)
shape_three.penup()
shape_three.speed(0)
shape_three.setposition(0,170)
#shape_three.lt(90)




def move_right():
    x = shape_two.xcor()
    x=x+10
    if x>=180:
        x=180
    shape_two.setx(x)


def move_left():
    x = shape_two.xcor()
    x=x-10
    if x<=-180:
        x=-180
    shape_two.setx(x)

def move_up():
    y=shape_two.ycor()
    y=y+10
    if y>=180:
        y=180
    shape_two.sety(y)


def move_down():
    y=shape_two.ycor()
    y=y-10
    if y<=-180:
        y=-180
    shape_two.sety(y)

def shoot():
    fire = turtle.Turtle()
    fire.hideturtle()
    fire.color("white")
    fire.shape("circle")
    fire.shapesize(1,1)
    fire.penup()
    fire.speed(10)
    x=shape_two.xcor()
    y=shape_two.ycor()
    fire.hideturtle()
    fire.setposition(x,y)
    fire.showturtle()
    fire.speed(2)
    fire.sety(y+400)
    fire.hideturtle()


    
turtle.listen()
turtle.onkey(move_right,"Right")
turtle.onkey(move_left,"Left")
turtle.onkey(move_up,"Up")
turtle.onkey(move_down,"Down")
turtle.onkey(shoot, "0")
enemyspeed=5
while True:

    x=shape_three.xcor()
    y=shape_three.ycor()

    x=x+enemyspeed
    if x>=180:
        enemyspeed=enemyspeed*-1
        y=y-10
    if x<=-180:
        enemyspeed=enemyspeed*-1
        y=y-10
        
    
    shape_three.setx(x)
    shape_three.sety(y)
 










 


 
