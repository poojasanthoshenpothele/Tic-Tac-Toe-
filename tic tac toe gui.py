import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text="", font=("Arial", 24), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.window.quit()
            elif all(all(cell != "" for cell in row) for row in self.board):
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.window.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]

        return None

    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()