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

        TYPE = "<class 'int'>"
        if str(type(int(positionVector[0]))) != TYPE and str(type(int(positionVector[1]))) != TYPE:
            return 33

        x = int(positionVector[0])-1
        y = int(positionVector[1])-1
        if x >= self.boardSize or y >= self.boardSize:
            print("max size is", self.boardSize)
            return 6
            
        if self.gameBoard[x][y] != "-":
            return 2

        self.gameBoard[x][y] = str(player).lower()
        self.check()

    def check(self):
        str_checks = None
        up_checks = None
        crs_checks = None
        checks = ["x", "o"]
        crs_c = []
        crs_r = []

        i = 0
        while 1:

            if i == self.boardSize:
                break

            rws = []
            crs_c.extend(self.gameBoard[i][i])
            crs_r.extend(self.gameBoard[i][self.boardSize-(i+1)])

            r = 0
            while 1:
                if r == self.boardSize:
                    break
                idt = self.gameBoard[r][i]
                rws.extend(idt)
                r += 1

            unique, counts = np.unique(self.gameBoard[i], return_counts=True)
            unique, counts = list(unique), list(counts)

            for C in checks:
                try:
                    _up_amm = rws.count(C)
                    _str_amm = counts[int(unique.index(C))]
                    up_comb = (C, _up_amm)
                    str_comb = (C, _str_amm)
                    if _up_amm == self.boardSize:
                        up_checks = up_comb
                    if _str_amm == self.boardSize:
                        str_checks = str_comb
                except:
                    pass
            i += 1

        for i in checks:
            try:
                _crs_amm1 = crs_c.count(i)
                _crs_amm2 = crs_r.count(i)

                comb_1 = (i._crs_amm1)
                comb_2 = (i._crs_amm2)

                if _crs_amm1 == self.boardSize:
                    crs_checks = comb_1

                if _crs_amm2 == self.boardSize:
                    crs_checks = comb_2
            except:
                pass

        cklp = [str_checks, up_checks, crs_checks]
        for i in cklp:
            if i != None:
                print(colored(i[0], "red"), "has won")
                self.curr_playing = False

    def display(self):
        xy_row = [format(i+1, "0%s" %(len(str(self.boardSize)))) for i in range(0, self.boardSize)]
        xyl_fmt = "/ "

        if self.boardSize >= 10:
            xyl_fmt+=" "

        print(colored(
            xyl_fmt+" ".join(xy_row), "yellow")
        )
        ms = ""
        for i in range(0, self.boardSize):
            itms = " ".join(self.gameBoard[i])
            if self.boardSize >= 10:              
                itms = itms.replace("-"," "+"-")

            Id = colored(format(i+1, "0%s" %
                                (len(str(self.boardSize)))), "yellow")
            ms+=f"{Id} {itms}\n".format()
        print(ms)
        self.check()
