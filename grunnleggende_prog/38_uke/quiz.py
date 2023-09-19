countries = {"Japan":"Tokyo","Norway":"Oslo","England":"London"}

def quiz():
    rounds = 0
    points = 0
    alternatives = [x for x in countries.values()]
    while True:
        for i in countries.keys():
            print(alternatives)
            answer = input(f"Whats the capital in {i}?\nSkriv her: ")
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