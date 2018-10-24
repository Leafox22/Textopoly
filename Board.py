from NewCmdCode import playerlist
from colored import fg, bg, attr, stylize

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

'''
Colours for the stuff
T   E   X   T   O   P   O   L   Y
1  166 208  3  22  76  26  13  54
'''

def printBoard():

    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|    ___   ___    |  "+fg(94)+"Old"+ attr("reset")+"   |        | "+fg(94)+"White"+ attr("reset")+"  | INCOME |"+fg(245)+"Kings. C"+ attr("reset")+"| "+fg(159)+"Angel"+ attr("reset")+"  |        | "+fg(159)+"Euston"+ attr("reset")+" | "+fg(159)+"Penton"+ attr("reset")+" |  Just Visiting  |")
    print("|   | _ | |   |   |"+fg(94)+"Kent Rd"+ attr("reset")+" |        | "+fg(94)+"Chapel"+ attr("reset")+" |  TAX   |"+fg(245)+"Station"+ attr("reset")+" | "+fg(159)+"Aisle"+ attr("reset")+"  |        |   "+fg(159)+"Rd"+ attr("reset")+"   |   "+fg(159)+"Rd"+ attr("reset")+"   |{}|".format(" ".join(boardSpace[10]).center(cf(10))))
    print("|   |_  | | | |   |  $60   | COMM.  |  $60   |Pay $200|  $200  |  $100  | CHANCE |  $100  |  $120  |_________________|")
    print("|    _| | | | |   |        | CHEST  |        |        |        |        |   ??   |        |        |     In  JAIL    |")
    print("|   /___| |___|   |        |        |        |        |        |        |        |        |        |    ||      ||   |")
    print("|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|    ||{}||   |".format(" ".join(boardSpace[0]).center(cf(0)), " ".join(boardSpace[1]).center(sf(1)), " ".join(boardSpace[2]).center(sf(2)),  " ".join(boardSpace[3]).center(sf(3)),  " ".join(boardSpace[4]).center(sf(4)),  " ".join(boardSpace[5]).center(sf(5)),  " ".join(boardSpace[6]).center(sf(6)),  " ".join(boardSpace[7]).center(sf(7)),  " ".join(boardSpace[8]).center(sf(8)),  " ".join(boardSpace[9]).center(sf(9)), " ".join(inJail).center(6 + (15*len(inJail)))))
    print("|  ------------>  |        |        |        |        |        |        |        |        |        |    ||      ||   |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|   "+fg(20)+"Mayfair"+ attr("reset")+"       |                                                                                |   "+fg(201)+"Pall Mall"+ attr("reset")+"     |")
    print("|     $400        |                                                                                |      $140       |")
    print("|{}|                                                                                |{}|".format(" ".join(boardSpace[39]).center(cf(39)), " ".join(boardSpace[11]).center(cf(11))))
    print("|                 |                                                                                |                 |")
    print("+--------+--------+                                                                                +--------+--------+")
    print("|   SUPER TAX     |               //////////////                                                   |   "+fg(146)+"Electic Co."+ attr("reset")+"   |")
    print("|    Pay $100     |              /            /                                                    |      $150       |")
    print("|{}|             /            /                                                     |{}|".format(" ".join(boardSpace[38]).center(cf(38)), " ".join(boardSpace[12]).center(cf(12))))
    print("|                 |            /    COMM.   /                                                      |                 |")
    print("+--------+--------+           /    CHEST   /                                                       +--------+--------+")
    print("|   "+fg(20)+"Park Lane"+ attr("reset")+"     |          /            /                                                        |   "+fg(201)+"Whitehall"+ attr("reset")+"     |")
    print("|     $350        |         /            /                                                         |      $140       |")
    print("|{}|        /            /                                                          |{}|".format(" ".join(boardSpace[37]).center(cf(37)), " ".join(boardSpace[13]).center(cf(13))))
    print("|                 |       //////////////                                                           |                 |")
    print("+--------+--------+                                                                                +--------+--------+")
    print("|   CHANCE        |                                                                                |   "+fg(201)+"North. Ave."+ attr("reset")+"   |")
    print("|                 |                  "+fg(1)+"_______"+ attr("reset")+"        "+fg(3)+"_"+ attr("reset")+"                     "+fg(13)+"_"+ attr("reset")+"                        |      $160       |")
    print("|{}|".format(" ".join(boardSpace[36]).center(cf(36))) + "                 "+fg(1)+"|__   __|"+ attr("reset")+"      "+fg(3)+"| |"+ attr("reset")+"                   "+fg(13)+"| |"+ attr("reset")+"                       |{}|".format(" ".join(boardSpace[14]).center(cf(14))))
    print("|                 |                    "+fg(1)+"| | "+ attr("reset")+""+fg(166)+"____"+ attr("reset")+""+fg(208)+"_  _"+ attr("reset")+""+fg(3)+"| |_  "+ attr("reset")+""+fg(22)+"___  "+ attr("reset")+""+fg(76)+"_ __   "+ attr("reset")+""+fg(26)+"___ "+ attr("reset")+""+fg(13)+"| |"+fg(54)+"_   _"+ attr("reset")+"                  |                 |")
    print("+--------+--------+                    "+fg(1)+"| |"+ attr("reset")+""+fg(166)+"/ _ \\"+ attr("reset")+""+fg(208)+" \/ /"+ attr("reset")+""+fg(3)+" __ "+ attr("reset")+""+fg(22)+"/ _ \\"+ attr("reset")+""+fg(76)+"| '_ \ "+ attr("reset")+""+fg(26)+"/ _ \\"+ attr("reset")+""+fg(13)+"| | "+ attr("reset")+""+fg(54)+"| | |"+ attr("reset")+"                 +--------+--------+")
    print("|   "+fg(245)+"Liver Station"+ attr("reset")+" |                    "+fg(1)+"| |  "+ attr("reset")+""+fg(166)+"__/"+ attr("reset")+""+fg(208)+">  <| "+ attr("reset")+""+fg(3)+"||  "+ attr("reset")+""+fg(22)+"(_) "+ attr("reset")+""+fg(76)+"| |_) | "+ attr("reset")+""+fg(26)+"(_) "+ attr("reset")+""+fg(13)+"| | "+ attr("reset")+""+fg(54)+"|_| |"+ attr("reset")+"                 |   "+fg(245)+"Mary Station"+ attr("reset")+"  |")
    print("|     $200        |                    "+fg(1)+"|_|"+ attr("reset")+""+fg(166)+"\___/"+ attr("reset")+""+fg(208)+"_/\_\\"+ attr("reset")+""+fg(3)+"\__ "+ attr("reset")+""+fg(22)+"\___/"+ attr("reset")+""+fg(76)+"| .__/ "+ attr("reset")+""+fg(26)+"\___/"+ attr("reset")+""+fg(13)+"|_|"+ attr("reset")+""+fg(54)+"\__, |"+ attr("reset")+"                 |      $200       |")
    print("|{}|".format(" ".join(boardSpace[35]).center(cf(35))) +"                                          "+fg(76)+"| |"+ attr("reset")+"             "+fg(54)+"__/ |"+ attr("reset")+"                 |{}|".format(" ".join(boardSpace[15]).center(cf(15))))
    print("|                 |                                          "+fg(76)+"|_|"+ attr("reset")+"            "+fg(54)+"|___/"+ attr("reset")+"                  |                 |")
    print("+--------+--------+                                                                                +--------+--------+")
    print("|   "+fg(70)+"Bond St"+ attr("reset")+"       |                                                                                |   "+fg(208)+"Bow Street"+ attr("reset")+"    |")
    print("|     $320        |                                                                                |      $180       |")
    print("|{}|                                                                                |{}|".format(" ".join(boardSpace[34]).center(cf(34)), " ".join(boardSpace[16]).center(cf(16))))
    print("|                 |                                                                                |                 |")
    print("+--------+--------+                                                                                +--------+--------+")
    print("|   COMM. CHEST   |                                                              //////////////    |   COMM. CHEST   |")
    print("|                 |                                                             /            /     |                 |")
    print("|{}|                                                            /            /      |{}|".format(" ".join(boardSpace[33]).center(cf(33)), " ".join(boardSpace[17]).center(cf(17))))
    print("|                 |                                                           /            /       |                 |")
    print("+--------+--------+                                                          /   CHANCE   /        +--------+--------+")
    print("|   "+fg(70)+"Oxford St"+ attr("reset")+"     |                                                         /            /         |   "+fg(208)+"Marlborough"+ attr("reset")+"   |")
    print("|     $300        |                                                        /            /          |      $180       |")
    print("|{}|                                                       /            /           |{}|".format(" ".join(boardSpace[32]).center(cf(32)), " ".join(boardSpace[18]).center(cf(18))))
    print("|                 |                                                      //////////////            |                 |")
    print("+--------+--------+                                                                                +--------+--------+")
    print("|   "+fg(70)+"Regent St."+ attr("reset")+"    |                                                                                |    "+fg(208)+"Vine St"+ attr("reset")+"      |")
    print("|     $300        |                                                                                |      $200       |")
    print("|{}|                                                                                |{}|".format(" ".join(boardSpace[31]).center(cf(31)), " ".join(boardSpace[19]).center(cf(19))))
    print("|                 |                                                                                |                 |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|    Go to Jail   |"+fg(220)+"Picadily"+ attr("reset")+"|  "+fg(146)+"Water"+ attr("reset")+" |"+fg(220)+"Coventry"+ attr("reset")+"| "+fg(220)+"Leich."+ attr("reset")+" | "+fg(245)+"Fench."+ attr("reset")+" |"+fg(196)+"Trafalga"+ attr("reset")+"| "+fg(196)+"Fleet"+ attr("reset")+"  |        | "+fg(196)+"Strand"+ attr("reset")+" |  Free Parking   |")
    print("|   __ O--π __    |        |  "+fg(146)+"Works"+ attr("reset")+" |   "+fg(220)+"St"+ attr("reset")+"   | "+fg(220)+"Square"+ attr("reset")+" |"+fg(245)+"Station"+ attr("reset")+" | "+fg(196)+"Square"+ attr("reset")+" |   "+fg(196)+"St"+ attr("reset")+"   |        |        |    ______       |")
    print("|  /  \    /  \   |  $280  |  $150  |  $260  |  $260  |  $200  |  $240  |  $220  | CHANCE |  $220  |   /|_||_\`.__   |")
    print("| |    ||||    |  |        |        |        |        |        |        |        |   ??   |        |  (   _    _ _\  |")
    print("|  \__/    \__/   |        |        |        |        |        |        |        |        |        |  =`-(_)--(_)-'  |")
    print("|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(" ".join(boardSpace[30]).center(cf(30)), " ".join(boardSpace[29]).center(sf(29)), " ".join(boardSpace[28]).center(sf(28)), " ".join(boardSpace[27]).center(sf(27)), " ".join(boardSpace[26]).center(sf(26)), " ".join(boardSpace[25]).center(sf(25)), " ".join(boardSpace[24]).center(sf(24)), " ".join(boardSpace[23]).center(sf(23)), " ".join(boardSpace[22]).center(sf(22)), " ".join(boardSpace[21]).center(sf(21)), " ".join(boardSpace[20]).center(cf(20))))
    print("|                 |        |        |        |        |        |        |        |        |        |                 |")
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
printBoard()
