import numpy as np
import pandas as pd

class Connect_4:
    Turns = 0

    def __init__(self, size = (7, 8)):
        self.board = np.zeros(size)
        print(self.board)
    
    def show(self):
        print(self.board)

    def P1Turn(self, pos):
        Connect_4.Turns += 1
        self.board[pos[0], pos[1]] = 1

    def p2Turn(self, pos):
        self.board[pos[0], pos[1]] = 2

    def WinCheck(self):
        if Connect_4.Turns>3:
            for i in range(self.board.shape[0]):
                for j in range(2, self.board.shape[1]-2):
                    if self.board[i][j] == key:
                        pass
            pass
        pass
        # return None