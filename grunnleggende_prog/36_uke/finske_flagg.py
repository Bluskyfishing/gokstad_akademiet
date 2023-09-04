import turtle 

t = turtle.Turtle()

#Hvit rektangel

def rektangel():
    turtle.Screen().bgcolor("black")
    t.speed(20)
    t.fillcolor("white")
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

#Blått kors Vertikal
t.up()
t.left(180)
t.forward(380)

t.fillcolor("dark blue")
t.begin_fill()

for side in range(0,2):
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(70) #Tykkelse 

t.end_fill()

#Blått kors Horizontal

t.forward(120)
t.right(90)
t.forward(120)
t.right(90)

t.begin_fill()

t.forward(500)
t.left(90)
t.forward(70) #Tykkelse 
t.left(90)
t.forward(500)
t.left(90)
t.forward(70) #Tykkelse 
t.right(180)
t.forward(30)

t.end_fill()

#Gjemme peker
t.fillcolor("black")
t.left(90)
t.forward(100)

#Kryss ut applikasjon.
turtle.exitonclick()