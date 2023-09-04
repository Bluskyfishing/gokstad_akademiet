import turtle 
t = turtle.Turtle()

def rektangel():
    turtle.Screen().bgcolor("black")
    t.speed(20)
    t.fillcolor("red")
    t.begin_fill()
    t.up()
    t.forward(200)
    t.down()

    for side in range(0,2):
        t.left(90)
        t.forward(300)
        t.left(90)
        t.forward(500)
    
    t.end_fill()

rektangel()

# hvit kors 
t.up()
t.left(180)
t.forward(380)

t.fillcolor("white")
t.begin_fill()

for side in range(0,2):
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(100)

t.end_fill()

t.forward(120)
t.right(90)
t.forward(100)
t.right(90)

t.begin_fill()

t.forward(500)
t.left(90)
t.forward(100)
t.left(90)
t.forward(500)
t.left(90)
t.forward(100)
t.right(180)
t.forward(30)

t.end_fill()

#Blått kross
t.fillcolor("blue")
t.begin_fill()

t.right(90)
t.forward(500)
t.left(90)
t.forward(40)
t.left(90)
t.forward(500)
t.left(90)
t.forward(40)

t.end_fill()



turtle.exitonclick()