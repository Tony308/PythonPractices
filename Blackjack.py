def blackjack(player1, player2):
    if player1 > 21 and player2 < 22:
        print ("Player 1 busts. Player 2 wins.")

    if player2 > 21 and player1 < 22:
        print ("Player 2 busts. Player 1 wins.")
        
    if player1 == player2:
        print("Draw.")
    if player1 < player2 and player2 < 22:
        print ("Player 2 wins.")
    elif player2 < player1 and player1 < 22:
        print ("Player 1 wins.")
