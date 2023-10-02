import turtle
import random as rnd

COLORS = ('yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan',
          'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray')

DIRECTION_RIGHT = 0
DIRECTION_UP = 90
DIRECTION_LEFT = 180
DIRECTION_DOWN = 270

START_X = -300
END_X = 300 
MIN_Y = -100
HEIGHT = 200

def create_turtle(color: str):
    t = turtle.Turtle()
    t.color(color)
    t.shape("turtle")
    return t 

def create_turtles(count: int):
    turtles = []
    for colr in rnd.sample(COLORS,count):
        turtles.append(create_turtle(colr))
    return turtles

def draw_line(trle: turtle.Turtle,
              startpos:(int,int),
              length: int,
              direction: int,
              text: str):
    trle.penup()
    trle.goto(startpos)
    trle.setheading(direction)
    trle.pendown()
    trle.forward(length)
    trle.write(text)

def write_results(draw_turtle: turtle.Turtle,
                  startpos: [int,int],
                  results: [turtle.Turtle]):
    draw_turtle.penup()
    draw_turtle.goto(startpos)
    draw_turtle.write("Result List:")
    
    x, y = startpos
    offset = -20
    y -= offset

    for idx, p in enumerate(results):
        draw_turtle.goto(x, y)
        draw_turtle.pencolor(p.color()[0])
        draw_turtle.write(f"Nr {idx + 1}: {p.color()[0]}")
        y -= 20

def sort_by_x_pos(t: turtle.Turtle):
    return t.xcor()