from turtle_race_header import * 



players = []
setup_turtle = turtle.Turtle()
screen = turtle.Screen()

def setup_game():
    global players, setup_turtle

    players = create_turtles(5)

    draw_line(setup_turtle,(START_X,MIN_Y),HEIGHT,DIRECTION_UP,"START")
    draw_line(setup_turtle,(END_X,MIN_Y),HEIGHT,DIRECTION_UP,"GOAL")

    offset = 50
    start = 0

    for t in players:
        t.penup()
        t.goto(START_X -20, start)
        start += offset



def game_loop():
    running = True
    is_player_finished = False

    while running:

        for p in players:
            p.forward(rnd.randint(1,20))
            x = p.xcor()
            if x > END_X:
                is_player_finished = True
        running = not is_player_finished
    game_end()

def run_game():
    global screen 

    res = turtle.numinput(title="Number of Players", prompt="How many players? (2-6)", 
                          default=2, minval=2, maxval=6)

    setup_game()

    screen.listen()
    screen.onkeypress(game_loop,"space")

    turtle.exitonclick()

def game_end():
    global setup_turtle
    
    result_list = sorted(players, key=sort_by_x_pos, reverse=True)
    write_results(setup_turtle, (-30,300) , result_list)


if __name__ == "__main__":
    run_game()