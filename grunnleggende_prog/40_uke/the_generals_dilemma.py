def game_loop():
    totalPlayer1Soldiers = 100
    totalPlayer2Soldiers = 100
    player1Score = 0
    player2Score = 0
    roundCounter = 1

    while True:
        print("\nRound:",roundCounter,"\n")
        try:
            player1Dispatched = int(input("Choose number of soldiers to be dispatched!: "))
            player2Dispatched = int(input("Choose number of soldiers to be dispatched!: "))
        except ValueError:
            print("Input not recognized! Try again")
            continue
        
        if player1Dispatched > totalPlayer1Soldiers or player2Dispatched > totalPlayer2Soldiers or player1Dispatched < 0 or player2Dispatched < 0: 
            print("Invalid value for amount of soldiers! Try again!")
            continue

        totalPlayer1Soldiers -= player1Dispatched
        totalPlayer2Soldiers -= player2Dispatched

        if player1Dispatched > player2Dispatched:
            player1Score += 1
            roundCounter += 1
            print("Player1 wins this round\n")
            print(f"The current score is:\nPlayer1:{player1Score}\nPlayer2:{player2Score}")            
        if player2Dispatched > player1Dispatched:
            player2Score += 1
            roundCounter += 1
            print("Player2 wins this round\n")
            print(f"The current score is:\nPlayer1:{player1Score}\nPlayer2:{player2Score}")
        if player1Score == 3 or player2Score == 3 or roundCounter == 6:
            print("\nThe game is finished!\n")

            if player1Score > player2Score:
                print(f"Player1 wins!\nWith a score of {player1Score}.")
            if player2Score > player1Score:
                print(f"Player2 wins!\nWith a score of {player2Score}.")

            playAgain = input("Do you want to play again?(Y/N): ").upper()

            if playAgain == "Y":
                    totalPlayer1Soldiers = 100
                    totalPlayer2Soldiers = 100
                    player1Score = 0
                    player2Score = 0
                    roundCounter = 1
            else:
                break

game_loop()