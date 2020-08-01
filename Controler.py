import nth_tac_toe

boardSize = 3

testGame = nth_tac_toe.Game(boardSize)

def X_manual():
    while 1:
        x_ip = input("x position:")
        x_ip = x_ip.split(" ")
        rc = testGame.updateBoard("x", x_ip)
        if rc == None:
            testGame.display()
            break


def O_manual():
    while 1:
        o_ip = input("o position:")
        o_ip = o_ip.split(" ")
        rc = testGame.updateBoard("o", o_ip)
        if rc == None:
            testGame.display()
            break


sd = 0
while 1:
    if sd == 0:
        testGame.display()
        sd += 1

    X_manual()
    if testGame.curr_playing == False:
        break

    O_manual()
    if testGame.curr_playing == False:
        break
