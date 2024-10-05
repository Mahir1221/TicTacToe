import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        # Initialize the main Tkinter window
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        # Game statistics variables
        self.games_played = 0
        self.player_wins = {'X': 0, 'O': 0, 'Tie': 0}

        # Initialize current player and game board
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # Initialize 2D list to hold Tkinter buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # Create buttons for the Tic Tac Toe grid
        for i in range(3):
            for j in range(3):
                # Lambda function to pass row and column values to make_move method
                self.buttons[i][j] = tk.Button(self.root, text='', font=('Helvetica', 24), width=6, height=2,
                                              command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

        # Bind keys to stop execution (Enter and Space keys)
        self.root.bind('<Return>', lambda event: self.stop_execution())
        self.root.bind('<space>', lambda event: self.stop_execution())

    def make_move(self, row, col):
        # Method to handle player moves
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED)

            # Check for a winner or a tie
            if self.check_winner():
                self.show_winner()
            elif self.is_board_full():
                self.show_tie()
            else:
                # Switch player turn
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Method to check if there's a winner
        for i in range(3):
            # Check rows and columns
            if all(self.board[i][j] == self.current_player for j in range(3)) or \
                    all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
                all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        # Check if the board is full
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def show_winner(self):
        # Method to display results when there's a winner
        self.player_wins[self.current_player] += 1
        self.games_played += 1
        self.show_results()

    def show_tie(self):
        # Method to display results when it's a tie
        self.player_wins['Tie'] += 1
        self.games_played += 1
        self.show_results()

    def show_results(self):
        # Method to display game results in a pop-up window
        results_message = f"Results after {self.games_played} games:\n"

        for player, wins in self.player_wins.items():
            if player == 'Tie':
                results_message += f"{player}: {wins} games\n"
            else:
                results_message += f"Player {player}: {wins} wins\n"

        result_dialog = tk.Toplevel(self.root)
        result_dialog.title("Game Results")

        result_label = tk.Label(result_dialog, text=results_message, font=('normal', 12))
        result_label.pack(padx=20, pady=20)

        ok_button = tk.Button(result_dialog, text="OK", command=lambda: (result_dialog.destroy(), self.new_game()))
        ok_button.pack(pady=10)

    def new_game(self):
        # Method to start a new game, reset the board and enable buttons
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='', state=tk.NORMAL)

    def stop_execution(self):
        # Method to stop the execution of the program
        raise SystemExit

    def run(self):
        # Method to start the Tkinter main loop
        self.root.mainloop()

# Check if the script is executed as the main program
if __name__ == "__main__":
    # Create an instance of the TicTacToeGUI class and run the game
    game = TicTacToeGUI()
    game.run()