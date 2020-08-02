import numpy as np
from termcolor import colored


class Game:

    curr_playing = True

    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.gameBoard = np.full((boardSize, boardSize), "-")

    def updateBoard(self, player, positionVector):
        if self.curr_playing == False:
            print("Game has ended")
            return 0

        if len(positionVector) != 2:
            print("enter two values")
            return 22


        TYPE = "<class 'int'>"
        if str(type(int(positionVector[0]))) != TYPE and str(type(int(positionVector[1]))) != TYPE:
            return 33

        try:
            x = int(positionVector[0])-1
            y = int(positionVector[1])-1
        except Exception:
            if x >= self.boardSize or y >= self.boardSize:
                print("max size is", self.boardSize)
                return 6
                
        if x >= self.boardSize or y >= self.boardSize:
            print("max size is", self.boardSize)
            return 6

        if self.gameBoard[x][y] != "-":
            return 2

        self.gameBoard[x][y] = str(player).lower()
        self.check()

    def check(self):
        chks = ["x", "o"]
        # hori check
        for i in range(0, self.boardSize):
            itms = "".join(self.gameBoard[i])
            for i in range(2):
                if itms.count(chks[i]) == len(itms):
                    print(colored(chks[i], "red"), "has won")
                    self.curr_playing = False
                    return
        # vert check
        for i in range(0, self.boardSize):
            itms = ""
            for j in range(0, self.boardSize):
                itms += self.gameBoard[j][i]
            for i in range(2):
                if itms.count(chks[i]) == len(itms):
                    print(colored(chks[i], "red"), "has won")
                    self.curr_playing = False
                    return

        # cross check 1
        itms = ""
        for j in range(0, self.boardSize):
            itms += self.gameBoard[j][j]

        for i in range(2):
            if itms.count(chks[i]) == len(itms):
                print(colored(chks[i], "red"), "has won")
                self.curr_playing = False
                return

        # cross check 2
        itms = ""
        rp = list(range(self.boardSize-1, -1, -1))

        for i in range(0, self.boardSize):
            itms += self.gameBoard[i][rp[i]]

        for i in range(2):
            if itms.count(chks[i]) == len(itms):
                print(colored(chks[i], "red"), "has won")
                self.curr_playing = False
                return

        #fill check
        if str(self.gameBoard).count("-") == 0:
            print(colored("No one", "red"), "has won")
            self.curr_playing = False
            return

    def display(self):
        xy_row = [format(i+1, "0%s" % (len(str(self.boardSize))))
                  for i in range(0, self.boardSize)]
        xyl_fmt = "/ "

        if self.boardSize >= 10:
            xyl_fmt += " "

        print(colored(
            xyl_fmt+" ".join(xy_row), "yellow")
        )
        ms = ""
        for i in range(0, self.boardSize):
            itms = " ".join(self.gameBoard[i])
            if self.boardSize >= 10:
                itms = itms.replace("-", " "+"-")
                itms = itms.replace("x", " "+"x")
                itms = itms.replace("o", " "+"o")
            itms = itms.replace("x",colored("x",attrs=["bold"],color="blue"))
            itms = itms.replace("o",colored("o",attrs=["bold"],color="red"))

            Id = colored(format(i+1, "0%s" %
                                (len(str(self.boardSize)))), "yellow")
            ms += f"{Id} {itms}\n".format()
        print(ms)
        self.check()
