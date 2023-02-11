import random

moves = []

class TicTacToe:
    def __init__(self):
        self.board = [[0 for row in range(3)] for column in range(3)] 
        self.win_conditions = []
        self.two_in_a_row = []
        
        self.players = [1, 2]
        random.shuffle(self.players)
       
        self.available_squares = [[0, 0], [0, 1], [0, 2],
                                  [1, 0], [1, 1], [1, 2],
                                  [2, 0], [2, 1], [2, 2]]    

    def random_play(self):
#        print(f"Player {self.players[0]}")
        
        count = 1
        game = []
        
        while self.should_continue():
            count+=1
            
            square = random.choice(self.available_squares)
            game.append(f"{self.players[0]}{self.available_squares.index(square)}")
            self.available_squares.remove(square)
            
            self.board[square[0]][square[1]] = self.players[0]
 #           print(f"{self.board[0]}\n{self.board[1]}\n{self.board[2]}\n")
            self.players.reverse()
        
        if game not in moves:
            moves.append(game)
        
        print(len(moves))
                
    def has_two_in_a_row(self):
        for i in range(3):
            # Horizontal
            self.two_in_a_row.append([self.board[i][0], self.board[i][1]])
            self.two_in_a_row.append([self.board[i][1], self.board[i][2]])
            
        for i in range(2):
            # Vertical
            self.two_in_a_row.append([self.board[i][0], self.board[i+1][0]])
            self.two_in_a_row.append([self.board[i][i+1], self.board[i+1][i+1]])
            self.two_in_a_row.append([self.board[i][2-i], self.board[i+1][2-i]])
            
            # Diagonal
            self.two_in_a_row.append([self.board[i][i], self.board[i+1][i+1]])        
            self.two_in_a_row.append([self.board[i+1][1-i], self.board[i][2-i]])
       
        for condition in self.two_in_a_row:
            if condition[0] == condition[1] == self.players[1]:
                return True
        
    def should_continue(self):
        for i in range(3):
            # Horizontal
            self.win_conditions.append([self.board[i][0], self.board[i][1], self.board[i][2]])
            # Vertical
            self.win_conditions.append([self.board[0][i], self.board[1][i], self.board[2][i]])
        
        # Diagonal
        self.win_conditions.append([self.board[0][0], self.board[1][1], self.board[2][2]])
        self.win_conditions.append([self.board[2][0], self.board[1][1], self.board[0][2]])
        
        for condition in self.win_conditions:
            if condition[0] == condition[1] == condition[2] != 0:
                return False

        if (0 not in self.board[0] and 
              0 not in self.board[1] and 
              0 not in self.board[2]): 
            return False

        else: 
            self.win_conditions = []
            return True

if __name__ == '__main__':
    for i in range(100000):
        game = TicTacToe()
        game.random_play()
       
