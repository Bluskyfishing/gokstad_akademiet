import turtle 

min_turtle = turtle.Turtle()

#Tegner figur
min_turtle.shape("turtle")

#Endre hastihet
min_turtle.speed(100)

#Vi går fremover min_turtle.goto(x,y)
min_turtle.fillcolor("blue")
min_turtle.begin_fill()
min_turtle.forward(200)
min_turtle.left(90)
min_turtle.forward(200)
min_turtle.left(90)
min_turtle.forward(200)
min_turtle.left(90)
min_turtle.forward(200)
min_turtle.left(90)
min_turtle.end_fill()
#Snu turtle 
min_turtle.right(135)

#Før vi går
min_turtle.fillcolor("red")
min_turtle.begin_fill()
min_turtle.penup()
min_turtle.forward(200)
min_turtle.left(135)
min_turtle.pendown()
min_turtle.pencolor("red")
min_turtle.circle(100)
min_turtle.end_fill()

min_turtle.penup()
min_turtle.fillcolor("green")
min_turtle.begin_fill()
min_turtle.left(100)
min_turtle.forward(400)
min_turtle.right(100)

min_turtle.pendown()
min_turtle.forward(100)
min_turtle.left(120)
min_turtle.forward(100)
min_turtle.left(120)
min_turtle.forward(100)
min_turtle.end_fill()

# avslutt med stil 
turtle.exitonclick()