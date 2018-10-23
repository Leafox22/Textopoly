from NewCmdCode import playerlist

boardSpace = []
housingSpace = []
inJail = []
for i in range(0,40):
    boardSpace.append([])
for i in playerlist:
    if i.position == 10:
        if i.injail == True:
            inJail.append(i.token)
        else:
            boardSpace[i.position].append(i.token)
    else:
        boardSpace[i.position].append(i.token)

def cf(i): #cf stands for Chunky Formula
    formula = 17 + (15 * len(boardSpace[i]))
    return formula

def sf(i): #sf stands for Skinny Formula
    formula = 8 + (15 * len(boardSpace[i]))
    return formula

def printBoard():

    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|    ___   ___    |  Old   |        | White  | INCOME |Kings. C| Angel  |        | Euston | Penton |  Just Visiting  |")
    print("|   | _ | |   |   |Kent Rd |        | Chapel |  TAX   |Station | Aisle  |        |   Rd   |   Rd   |{}|".format("".join(boardSpace[10]).center(cf(10))))
    print("|   |_  | | | |   |  $60   | COMM.  |  $60   |Pay $200|  $200  |  $100  | CHANCE |  $100  |  $120  |_________________|")
    print("|    _| | | | |   |        | CHEST  |        |        |        |        |   ??   |        |        |     In  JAIL    |")
    print("|   /___| |___|   |        |        |        |        |        |        |        |        |        |    ||      ||   |")
    print("|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|    ||{}||   |".format("".join(boardSpace[0]).center(cf(0)), "".join(boardSpace[1]).center(sf(1)), "".join(boardSpace[2]).center(sf(2)),  "".join(boardSpace[3]).center(sf(3)),  "".join(boardSpace[4]).center(sf(4)),  "".join(boardSpace[5]).center(sf(5)),  "".join(boardSpace[6]).center(sf(6)),  "".join(boardSpace[7]).center(sf(7)),  "".join(boardSpace[8]).center(sf(8)),  "".join(boardSpace[9]).center(sf(9)), "".join(inJail).center(6 + (15 * len(inJail)))))
    print("|  ------------>  |        |        |        |        |        |        |        |        |        |    ||      ||   |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|   Mayfair       |                                                                                |   Pall Mall     |")
    print("|     $400        |                                                                                |      $140       |")
    print("|{}|                                                                                |{}|".format("".join(boardSpace[39]).center(cf(39)), "".join(boardSpace[11]).center(cf(11))))
    print("|                 |                                                                                |                 |")
    print("+--------+--------+                                                                                +--------+--------+")
    print("|   SUPER TAX     |               //////////////                                                   |   Electic Co.   |")
    print("|    Pay $100     |              /            /                                                    |      $150       |")
    print("|{}|             /            /                                                     |{}|".format("".join(boardSpace[38]).center(cf(38)), "".join(boardSpace[12]).center(cf(12))))
    print("|                 |            /    COMM.   /                                                      |                 |")
    print("+--------+--------+           /    CHEST   /                                                       +--------+--------+")
    print("|   Park Lane     |          /            /                                                        |   Whitehall     |")
    print("|     $350        |         /            /                                                         |      $140       |")
    print("|{}|        /            /                                                          |{}|".format("".join(boardSpace[37]).center(cf(37)), "".join(boardSpace[13]).center(cf(13))))
    print("|                 |       //////////////                                                           |                 |")
    print("+--------+--------+                                                                                +--------+--------+")
    print("|   CHANCE        |                                                                                |   North. Ave.   |")
    print("|                 |                  _______        _                     _                        |      $160       |")
    print("|{}|                 |__   __|      | |                   | |                       |{}|".format("".join(boardSpace[36]).center(cf(36)), "".join(boardSpace[14]).center(cf(14))))
    print("|                 |                    | | _____  _| |_  ___  _ __   ___ | |_   _                  |                 |")
    print("+--------+--------+                    | |/ _ \ \/ / __ / _ \| '_ \ / _ \| | | | |                 +--------+--------+")
    print("|   Liver Station |                    | |  __/>  <| ||  (_) | |_) | (_) | | |_| |                 |   Mary Station  |")
    print("|     $200        |                    |_|\___/_/\_\\\__ \___/| .__/ \___/|_|\__, |                 |      $200       |")
    print("|{}|                                          | |             __/ |                 |{}|".format("".join(boardSpace[35]).center(cf(35)), "".join(boardSpace[15]).center(cf(15))))
    print("|                 |                                          |_|            |___/                  |                 |")
    print("+--------+--------+                                                                                +--------+--------+")
    print("|   Bond St       |                                                                                |   Bow Street    |")
    print("|     $320        |                                                                                |      $180       |")
    print("|{}|                                                                                |{}|".format("".join(boardSpace[34]).center(cf(34)), "".join(boardSpace[16]).center(cf(16))))
    print("|                 |                                                                                |                 |")
    print("+--------+--------+                                                                                +--------+--------+")
    print("|   COMM. CHEST   |                                                              //////////////    |   COMM. CHEST   |")
    print("|                 |                                                             /            /     |                 |")
    print("|{}|                                                            /            /      |{}|".format("".join(boardSpace[33]).center(cf(33)), "".join(boardSpace[17]).center(cf(17))))
    print("|                 |                                                           /            /       |                 |")
    print("+--------+--------+                                                          /   CHANCE   /        +--------+--------+")
    print("|   Oxford St     |                                                         /            /         |   Marlborough   |")
    print("|     $300        |                                                        /            /          |      $180       |")
    print("|{}|                                                       /            /           |{}|".format("".join(boardSpace[32]).center(cf(32)), "".join(boardSpace[18]).center(cf(18))))
    print("|                 |                                                      //////////////            |                 |")
    print("+--------+--------+                                                                                +--------+--------+")
    print("|   Regent St.    |                                                                                |    Vine St      |")
    print("|     $300        |                                                                                |      $200       |")
    print("|{}|                                                                                |{}|".format("".join(boardSpace[31]).center(cf(31)), "".join(boardSpace[19]).center(cf(19))))
    print("|                 |                                                                                |                 |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|    Go to Jail   |Picadily|  Water |Coventry| Leich. | Fench. |Trafalga| Fleet  |        | Strand |  Free Parking   |")
    print("|   __ O--π __    |        |  Works |   St   | Square |Station | Square |   St   |        |        |    ______       |")
    print("|  /  \    /  \   |  $280  |  $150  |  $260  |  $260  |  $200  |  $240  |  $220  | CHANCE |  $220  |   /|_||_\`.__   |")
    print("| |    ||||    |  |        |        |        |        |        |        |        |   ??   |        |  (   _    _ _\  |")
    print("|  \__/    \__/   |        |        |        |        |        |        |        |        |        |  =`-(_)--(_)-'  |")
    print("|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format("".join(boardSpace[30]).center(cf(30)), "".join(boardSpace[29]).center(sf(29)), "".join(boardSpace[28]).center(sf(28)), "".join(boardSpace[27]).center(sf(27)), "".join(boardSpace[26]).center(sf(26)), "".join(boardSpace[25]).center(sf(25)), "".join(boardSpace[24]).center(sf(24)), "".join(boardSpace[23]).center(sf(23)), "".join(boardSpace[22]).center(sf(22)), "".join(boardSpace[21]).center(sf(21)), "".join(boardSpace[20]).center(cf(20))))
    print("|                 |        |        |        |        |        |        |        |        |        |                 |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
printBoard()
