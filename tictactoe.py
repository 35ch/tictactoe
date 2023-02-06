import tkinter
import random

class TicTacToe:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.resizable(0,0)        
        
        self.board = [[0 for row in range(3)] for column in range(3)] 
        self.buttons = [[tkinter.Button(self.window, disabledforeground="black") for row in range(3)] for column in range(3)]
        
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(height=1, width=2, font=("Helvetica 40 bold"), 
                                                 command=lambda row=row, column=column: self.play(row, column))
                self.buttons[row][column].grid(row=row, column=column)
        
        self.win_conditions = []
        
        self.players = ["X", "O"]
        random.shuffle(self.players)
        
        self.window.mainloop()

    def play(self, row, column):
        self.buttons[row][column].config(text = self.players[0], state = "disable")
        self.board[row][column] = self.players[0]
        self.players.reverse() 
        
        self.check_win()
    
    def check_win(self):
        for i in range(3):
            self.win_conditions.append([self.board[i][0], self.board[i][1], self.board[i][2]])
            self.win_conditions.append([self.board[0][i], self.board[1][i], self.board[2][i]])
        
        self.win_conditions.append([self.board[0][0], self.board[1][1], self.board[2][2]])
        self.win_conditions.append([self.board[2][0], self.board[1][1], self.board[0][2]])
        
        for condition in self.win_conditions:
            if condition[0] == condition[1] == condition[2] != 0:
                print(f"{self.players[1]} won!")
                exit()

        if (0 not in self.board[0] and 
              0 not in self.board[1] and 
              0 not in self.board[2]): 
            print("Draw")
            exit()     
        
        else: 
            self.win_conditions = []

TicTacToe()
