countries = {"Japan":"Tokyo","Norway":"Oslo","England":"London"}

def quiz():
    rounds = 0
    points = 0

    while True:
        for i in countries.keys():
            answer = input(f"Whats the capital in {i}?\n")
            rounds += 1
            if answer == countries[i]:
                print("Correct! Next question!\n")   
                points += 1    
            else:
                print("Wrong! Next question!\n")
        if rounds == 3:
            print(f"The quiz is over! You got {points} correct out of {rounds}.")
            break

quiz()