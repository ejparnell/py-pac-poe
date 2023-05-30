class TicTacToe():
    """
      This class represents a game of Tic Tac Toe
    """
    def __init__(self):
        """
        This method initializes the game
        """
        # Set the turn to None
        self.turn = None
        # Set the players to a dictionary
        # Key 1 = X player 1
        # Key -1 = O player 2
        # Key 0 = empty square
        self.players = {1: "X", -1: "O", 0: " "}
      
        # Set the board to a dictionary
        # All squares are empty to start
        self.board = {
            "A1": 0,
            "A2": 0,
            "A3": 0,
            "B1": 0,
            "B2": 0,
            "B3": 0,
            "C1": 0,
            "C2": 0,
            "C3": 0,
        }

        # Set the winning combos to a list of tuples
        self.winning_combos = [
          ("A1", "B1", "C1"),
          ("A2", "B2", "C2"),
          ("A3", "B3", "C3"),
          ("A1", "A2", "A3"),
          ("B1", "B2", "B3"),
          ("C1", "C2", "C3"),
          ("A1", "B2", "C3"),
          ("A3", "B2", "C1"),
        ]

    def show_greeting(self):
        """
        This method prints a greeting
        """
        print("----------------------")
        print("let's Play Py-Pac-Poe")
        print("----------------------")
    
    def get_turn(self):
      """
        This method prompts the user to select
        which player goes first
      """
      # Set the selection to None
      selection = None
      
      # Get the keys and values from the players dictionary
      player_keys = tuple(self.players.keys())[:-1]
      # Get the values from the players dictionary
      player_values = tuple(self.players.values())[:-1]

        # Loop until the user selects a valid player
      while not selection or selection not in player_values:
        # Prompt the user to select a player
        selection = input(f"Please Select Which Player Goes First (example X or O): ").upper()
        # Check if the selection is not in the player values
        if selection not in player_values:
          # Print an error message
          print("You Must Choose X or O")
    # Set the turn to the player key that matches the player value
      self.turn = player_keys[player_values.index(selection)]

    def get_move(self):
        """
        This method prompts the user to select a move
        """
        # Set the move to None
        move = None
        # Set move_valid to False
        move_valid = False
        # Set move_unavailable to False
        move_unavailable = True

        # Loop until the user selects a valid move
        while not move_valid or move_unavailable:
            # Prompt the user to select a move
            move = input(
                f"Player {self.players[self.turn]}'s Move (example B2): "
            ).upper()

            # Check if the move is valid
            move_valid = move in self.board
            # Check if the move is available
            move_unavailable = move_valid and self.board[move] != 0

            # If the move is not valid
            if not move_valid:
                # Print an error message
                print("Please Enter A Valid Move")
            # If the move is valid but unavailable
            elif move_unavailable:
                # Print an error message
                print("That Square Has Been Taken")
        # Return the move
        return move

    def print_board(self):
        """
        This method prints the current state
        of the board to the console
        """

        # Get the players
        player = self.players
        # Get the board
        board = self.board

        # Print the board
        print(f"""
             A   B   C
          1) {player[board["A1"]]} | {player[board["B1"]]} | {player[board["C1"]]}
            ------------
          2) {player[board["A2"]]} | {player[board["B2"]]} | {player[board["C2"]]}
            ------------
          3) {player[board["A3"]]} | {player[board["B3"]]} | {player[board["C3"]]}
        """)

    def get_winner(self):
        """
        This method calculates values placed
        at the designated positions in the winning combos list and evaluates if their absolute value equal 3, which means there are three matching values in those positions ... i.e -1 + -1 + -1 or 1 + 1 + 1
        """
        # Get the winning combos
        combos = self.winning_combos
        # Get the board
        board = self.board

        # Get the values from the board
        board_val_list = self.board.values()
        # Set the winner to False
        winner = False

        # Loop through the winning combos
        for combo in combos:
          # Do we have three matching values in a row?
          # Check if the absolute value of the sum of the values in the winning combo equal 3
          if abs(board[combo[0]] + board[combo[1]] + board[combo[2]]) == 3:
            # Set the winner to the value of the first square in the winning combo
            winner = self.turn; break
          # Let's check if all squares are occupied
          # Check if all values in the board value list are not equal to 0
          if all(v != 0 for v in board_val_list):
            # Set the winner to "T" for tie
            winner = "T" # Must be a tie
        # Return the winner
        return winner

    def play_game(self):
        """
        This method calls all appropriate instance methods
        to facilitate the game
        """      

        # Show the greeting
        self.show_greeting()
        # Print the board
        self.print_board()
        # Get the turn
        self.get_turn()

        # Set the players
        player = self.players
        # Set the winner to False
        winner = False

        # Loop until there is a winner
        while not winner:
            # Get the move
            self.board[self.get_move()] = self.turn
            # Print the board
            self.print_board()

            # Get the winner
            winner = self.get_winner()

            # Check if there is a winner
            if winner == "T":
              # Print a message
              print(f"It's a Tie Game"); break
            # Check if there is a winner
            elif winner != False:
              # Print a message
              print(f"Congratulations {player[winner]}!"); break
            # Switch the turn
            self.turn *= -1

# Instantiate the game class
TicTacToe().play_game()