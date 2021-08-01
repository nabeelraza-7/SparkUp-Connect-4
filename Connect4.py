import numpy as np
import pandas as pd
import sys

class Connect_4:
    Turns = 0

    def __init__(self, size = (7, 7), connect = 4):
        self.board = np.empty(size)
        self.board[:] = np.nan
        self.connectDots = connect
        # print(self.board)
    
    def show(self):
        print(self.board)

    def P1Turn(self, pos):
        # try:
        #     print(self.board[pos[0], pos[1]])
            if not self.board[pos[0], pos[1]] in [1, 2]:
                self.board[pos[0], pos[1]] = 1
                self.WinCheck()
            # else:
            #     raise Exception("Wrong input")
            Connect_4.Turns += 1
        # except:
        #     print("Wrong input, Try again", self.board[pos[0], pos[1]])
        #     self.show()
            # self.P1Turn((int(input("1: Enter row: ")), int(input("1: Enter col: "))))

    def P2Turn(self, pos):
        # try:
            if not self.board[pos[0], pos[1]] in [1, 2]:
                self.board[pos[0], pos[1]] = 2
                self.WinCheck()
        #     else:
        #         raise Exception("Wrong input, Try again...")
        # except:
        #     print("Wrong input, Try again", self.board[pos[0], pos[1]])
        #     self.show()
            # self.P2Turn((int(input("2: Enter row: ")), int(input("2: Enter col: "))))

    # def TiltCheck(self):
    #     i, j = 0, 3
    #     while True:
    #         if j<6:
    #             j+=1
    #         elif i<4:
    #             i+=1
    #         else:
    #             break
    #         I, J = i, j
    #         while True:
    #             print()
    #             break
    #     return Mat

    def WinCheck(self):
        if Connect_4.Turns>2:
            key1 = np.nan
            key2 = np.nan
            countR = 0
            countD = 0
            for i in range(self.board.shape[0]):
                for j in range(self.board.shape[1]):
                    if self.board[i, j] in [1, 2]:
                        if self.board[i, j] == key1:
                            countR += 1
                            if countR == 4:
                                print('Player', key1,'Won')
                                # sys.exit()
                        else:
                            countR = 1
                            key1 = self.board[i, j]
                    else:
                        countR = 0
                    if self.board[j, i] in [1, 2]:
                        if self.board[j, i] == key2:
                            countD += 1
                            if countD == 4:
                                print('Player', key2,'Won')
                                # sys.exit()
                        else:
                            countD = 1
                            key2 = self.board[i, j]
                    else:
                        countD = 0


A = None

# A.show()

# while True:
    # A.P1Turn((int(input("1: Enter row: ")), int(input("1: Enter col: "))))
    # A.show()
    # A.P2Turn((int(input("2: Enter row: ")), int(input("2: Enter col: "))))
    # A.show()