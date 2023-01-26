import tkinter

class TicTacToe:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.resizable(0,0)

        self.buttons = [[tkinter.Button(self.window) for row in range(3)] for column in range(3)]
        self.board = [[0 for row in range(3)] for column in range(3)] # Board to keep track of the game
        self.players = ["X", "O"]
        
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(height = 5, width = 10,
                    command = lambda row=row, column=column: self.play(row, column))
                self.buttons[row][column].grid(row = row, column = column)

        self.window.mainloop()

    def play(self, row, column):
        if self.players[0] == "X":
            self.buttons[row][column].config(text = self.players[0], state = "disable")
            self.board[row][column] = "X"
            self.players = self.players[::-1] # Reverses the player list
        else:
            self.buttons[row][column].config(text = self.players[0], state = "disable")
            self.board[row][column] = "O"
            self.players = self.players[::-1]
        
        self.check_win()
    
    def full_row(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != 0:
                return True
        return False
            
    def full_column(self):
        for r in range(3):
            if self.board[0][r] == self.board[1][r] == self.board[2][r] != 0:
                return True
        return False

    def full_diagonal(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:            
            return True
        return False
    
    def check_win(self):
        if self.full_row() or self.full_column() or self.full_diagonal():
            print(f"{self.players[1]} won!")
            self.window.destroy()
        
        elif 0 not in self.board[0] and 0 not in self.board[1] and 0 not in self.board[2]:
            print("Draw")
            self.window.destroy()

TicTacToe()
