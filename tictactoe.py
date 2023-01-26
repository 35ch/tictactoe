import tkinter

class TicTacToe:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Tic-Tac-Toe")

        self.buttons = [[tkinter.Button(self.window) for row in range(3)] for column in range(3)]
        self.board = [[0 for row in range(3)] for column in range(3)]
        
        print(self.board)
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(height = 5, width = 10, command = lambda row=row, column=column: self.play(row, column))
                self.buttons[row][column].grid(row = row, column = column)

        self.player = "X"
        self.window.mainloop()

    def play(self, row, column):
        if self.player == "X":
            self.buttons[row][column].config(text = "X", state = "disable")
            self.board[row][column] = "X"
            self.player = "O"
        else:
            self.buttons[row][column].config(text = "O", state = "disable")
            self.board[row][column] = "O"
            self.player = "X"
        self.check_win()
        print(self.board)
    
    def full_row(self):
        for row in self.board:
            for player in ["X", "O"]:
                if row[0] == row[1] == row[2] == player:
                    print (f"{player} won!")
        return False
            
    def full_column(self):
        for player in ["X", "O"]:
            for r in range(3):
                if self.board[0][r] == self.board[1][r] == self.board[2][r] == player:
                    print(f"{player} won!")
        return False

    def full_diagonal(self):
        for player in ["X", "O"]:
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
                print(f"{player} won!")
            elif self.board[0][2] == self.board[1][1] == self.board[2][0] == player:            
                print(f"{player} won!")
        return False
    
    def check_win(self):
        if 0 not in self.board[0] and 0 not in self.board[1] and 0 not in self.board[2]:
            print("Draw")
            self.window.destroy()
        
        if self.full_row() or self.full_column() or self.full_diagonal():
            self.window.destroy()

TicTacToe()
