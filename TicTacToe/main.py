from TicTacToe.tic_tac_toe import TicTacToe

if __name__ == "__main__":
    game = TicTacToe()
    game.initializeGame()
    print("Game winner is " + game.startGame())