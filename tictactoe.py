import tkinter
import random

class TicTacToe:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.resizable(0,0)

        self.buttons = [[tkinter.Button(self.window) for row in range(3)] for column in range(3)]
        self.board = [[0 for row in range(3)] for column in range(3)] 
        
        self.players = ["X", "O"]
        random.shuffle(self.players)
        
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(height = 5, width = 10, command = lambda
                                                 row=row, column=column: self.play(row, column))
                self.buttons[row][column].grid(row = row, column = column)

        self.window.mainloop()

    def play(self, row, column):
        self.buttons[row][column].config(text = self.players[0], state = "disable")
        self.board[row][column] = self.players[0]
        self.players.reverse() 

        self.check_win()
    
    def print_result(self):
        print(f"{self.players[1]} won!")
        self.window.destroy()
    
    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                self.print_result()
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                self.print_result()
 
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != 0 or 
            self.board[0][2] == self.board[1][1] == self.board[2][0] != 0): 
            self.print_result()

        elif (0 not in self.board[0] and 
              0 not in self.board[1] and 
              0 not in self.board[2]): 
            print("Draw")
            self.window.destroy()

TicTacToe()
