f = [0,1]

for i in range(1,10):
    f.append(f[i]+f[i-1])
f = tuple (f)
print(f)


from meoreSakitxi import func

func(int(input("shemoitane ricxvi: ")))


print("spaceze ar imushava chemtan da m gilakze gavakete)")

import turtle
win = turtle.Screen()
win.bgcolor("White")
win.setup(800,800)

shape = turtle.Turtle()
shape.color("black")
shape.shape("turtle")
shape.pendown()


def right():
    x = shape.xcor()
    x = x + 10
    shape.setx(x)

def left():
    x = shape.xcor()
    x= x - 10
    shape.setx(x)

def up():
    y = shape.ycor()
    y = y + 10
    shape.sety(y)

def down():
    y = shape.ycor()
    y = y - 10
    shape.sety(y)

def erase() :
    shape.clear()

    
turtle.listen()
turtle.onkey(right,"Right")
turtle.onkey(left,"Left")
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(erase,"m")

    
