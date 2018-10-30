from NewCmdCode import playerlist
from colored import fg, bg, attr, stylize
from NewCmdCode import gameboard

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

def housePrint(level, tileSize):
    if tileSize == "small":
        if (level < 5) and (level >= 1):
            return ("✧ "*level).center(8)
        elif level == 5:
            return ("✦"*5).center(8)
        else:
            return " ".center(8)

    elif tileSize == "big":
        if (level < 5) and (level >= 1):
            return("✧ "*level).center(17)
        elif level == 5:
            return ("✦"*5).center(17)
        else:
            return " ".center(17)


def printBoard():

    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|    ___   ___    |  "+fg(94)+"S23"+ attr("reset")+"   |        |  "+fg(94)+"S24"+ attr("reset")+"   | INCOME |"+fg(245)+"Kings. C"+ attr("reset")+"|   "+fg(159)+"M1"+ attr("reset")+"   |        |   "+fg(159)+"M2"+ attr("reset")+"   |   "+fg(159)+"M3"+ attr("reset")+"   |  Just Visiting  |")
    print("|   | _ | |   |   |        |        |        |  TAX   |"+fg(245)+"Station"+ attr("reset")+" |        |        |        |        |{}|".format(" ".join(boardSpace[10]).center(cf(10))))
    print("|   |_  | | | |   |  $60   | COMM.  |  $60   |Pay $200|  $200  |  $100  | CHANCE |  $100  |  $120  |_________________|")
    print("|    _| | | | |   |        | CHEST  |        |        |        |        |   ??   |        |        |    DETENTION    |")
    print("|   /___| |___|   |        |        |        |        |        |        |        |        |        |    ||      ||   |")
    print("|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|    ||{}||   |".format(" ".join(boardSpace[0]).center(cf(0)), " ".join(boardSpace[1]).center(sf(1)), " ".join(boardSpace[2]).center(sf(2)),  " ".join(boardSpace[3]).center(sf(3)),  " ".join(boardSpace[4]).center(sf(4)),  " ".join(boardSpace[5]).center(sf(5)),  " ".join(boardSpace[6]).center(sf(6)),  " ".join(boardSpace[7]).center(sf(7)),  " ".join(boardSpace[8]).center(sf(8)),  " ".join(boardSpace[9]).center(sf(9)), " ".join(inJail).center(6 + (15*len(inJail)))))
    print("|  ------------>  |{}|        |{}|        |        |{}|        |{}|{}|    ||      ||   |".format(housePrint(gameboard[1].level,"small"), housePrint(gameboard[3].level,"small"), housePrint(gameboard[6].level,"small"), housePrint(gameboard[8].level,"small"), housePrint(gameboard[9].level,"small")))
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|     "+fg(20)+"Café 12"+ attr("reset")+"     |                                                                                |  "+fg(201)+"Staff Room 1"+ attr("reset")+"   |")
    print("|      $400       |                                                                                |      $140       |")
    print("|{}|                                                                                |{}|".format(" ".join(boardSpace[39]).center(cf(39)), " ".join(boardSpace[11]).center(cf(11))))
    print("|{}|                                                                                |{}|".format(housePrint(gameboard[39].level,"big"), housePrint(gameboard[11].level,"big")))
    print("+--------+--------+                                                                                +--------+--------+")
    print("|   SUPER TAX     |               "+fg(11)+"//////////////"+ attr("reset")+"                                                   |  "+fg(146)+"Uniform Shop"+ attr("reset")+"   |")
    print("|    Pay $100     |              "+fg(11)+"/            /"+ attr("reset")+"                                                    |      $150       |")
    print("|{}|".format(" ".join(boardSpace[38]).center(cf(38))) + "             "+fg(11)+"/            /"+ attr("reset")+"                                                     |{}|".format(" ".join(boardSpace[12]).center(cf(12))))
    print("|                 |            "+fg(11)+"/    COMM.   /"+ attr("reset")+"                                                      |                 |")
    print("+--------+--------+           "+fg(11)+"/    CHEST   /"+ attr("reset")+"                                                       +--------+--------+")
    print("|  "+fg(20)+"Allawah Shops"+ attr("reset")+"  |          "+fg(11)+"/            /"+ attr("reset")+"                                                        |  "+fg(201)+"Staff Room 2"+ attr("reset")+"   |")
    print("|      $350       |         "+fg(11)+"/            /"+ attr("reset")+"                                                         |      $140       |")
    print("|{}|".format(" ".join(boardSpace[37]).center(cf(37)))  + "        "+fg(11)+"/            /"+ attr("reset")+"                                                          |{}|".format(" ".join(boardSpace[13]).center(cf(13))))
    print("|{}|       ".format(housePrint(gameboard[37].level,"big"))+fg(11)+"//////////////"+ attr("reset")+"                                                           |{}|".format(housePrint(gameboard[13].level,"big")))
    print("+--------+--------+                                                                                +--------+--------+")
    print("|     CHANCE      |                                                                                |  "+fg(201)+"Staff Room 3"+ attr("reset")+"   |")
    print("|                 |                  "+fg(1)+"_______"+ attr("reset")+"        "+fg(3)+"_"+ attr("reset")+"                     "+fg(13)+"_"+ attr("reset")+"                        |      $160       |")
    print("|{}|".format(" ".join(boardSpace[36]).center(cf(36))) + "                 "+fg(1)+"|__   __|"+ attr("reset")+"      "+fg(3)+"| |"+ attr("reset")+"                   "+fg(13)+"| |"+ attr("reset")+"                       |{}|".format(" ".join(boardSpace[14]).center(cf(14))))
    print("|                 |                    "+fg(1)+"| | "+ attr("reset")+""+fg(166)+"____"+ attr("reset")+""+fg(208)+"_  _"+ attr("reset")+""+fg(3)+"| |_  "+ attr("reset")+""+fg(22)+"___  "+ attr("reset")+""+fg(76)+"_ __   "+ attr("reset")+""+fg(26)+"___ "+ attr("reset")+""+fg(13)+"| |"+fg(54)+"_   _"+ attr("reset")+"                  |{}|".format(housePrint(gameboard[14].level,"big")))
    print("+--------+--------+                    "+fg(1)+"| |"+ attr("reset")+""+fg(166)+"/ _ \\"+ attr("reset")+""+fg(208)+" \/ /"+ attr("reset")+""+fg(3)+" __ "+ attr("reset")+""+fg(22)+"/ _ \\"+ attr("reset")+""+fg(76)+"| '_ \ "+ attr("reset")+""+fg(26)+"/ _ \\"+ attr("reset")+""+fg(13)+"| | "+ attr("reset")+""+fg(54)+"| | |"+ attr("reset")+"                 +--------+--------+")
    print("|  "+fg(245)+"Liver Station"+ attr("reset")+"  |                    "+fg(1)+"| |  "+ attr("reset")+""+fg(166)+"__/"+ attr("reset")+""+fg(208)+">  <| "+ attr("reset")+""+fg(3)+"||  "+ attr("reset")+""+fg(22)+"(_) "+ attr("reset")+""+fg(76)+"| |_) | "+ attr("reset")+""+fg(26)+"(_) "+ attr("reset")+""+fg(13)+"| | "+ attr("reset")+""+fg(54)+"|_| |"+ attr("reset")+"                 |   "+fg(245)+"Mary Station"+ attr("reset")+"  |")
    print("|      $200       |                    "+fg(1)+"|_|"+ attr("reset")+""+fg(166)+"\___/"+ attr("reset")+""+fg(208)+"_/\_\\"+ attr("reset")+""+fg(3)+"\__ "+ attr("reset")+""+fg(22)+"\___/"+ attr("reset")+""+fg(76)+"| .__/ "+ attr("reset")+""+fg(26)+"\___/"+ attr("reset")+""+fg(13)+"|_|"+ attr("reset")+""+fg(54)+"\__, |"+ attr("reset")+"                 |      $200       |")
    print("|{}|".format(" ".join(boardSpace[35]).center(cf(35))) +"                                          "+fg(76)+"| |"+ attr("reset")+"             "+fg(54)+"__/ |"+ attr("reset")+"                 |{}|".format(" ".join(boardSpace[15]).center(cf(15))))
    print("|                 |                                          "+fg(76)+"|_|"+ attr("reset")+"            "+fg(54)+"|___/"+ attr("reset")+"                  |                 |")
    print("+--------+--------+                                                                                +--------+--------+")
    print("|    "+fg(70)+"The Hall"+ attr("reset")+"     |                                                                                |       "+fg(208)+"S8"+ attr("reset")+"        |")
    print("|      $320       |                                                                                |      $180       |")
    print("|{}|                                                                                |{}|".format(" ".join(boardSpace[34]).center(cf(34)), " ".join(boardSpace[16]).center(cf(16))))
    print("|{}|                                                                                |{}|".format(housePrint(gameboard[34].level,"big"), housePrint(gameboard[16].level,"big")))
    print("+--------+--------+                                                                                +--------+--------+")
    print("|   COMM. CHEST   |                                                              "+fg(202)+"//////////////"+ attr("reset")+"    |   COMM. CHEST   |")
    print("|                 |                                                             "+fg(202)+"/            /"+ attr("reset")+"     |                 |")
    print("|{}|".format(" ".join(boardSpace[33]).center(cf(33)))+"                                                            "+fg(202)+"/            /"+ attr("reset")+"      |{}|".format(" ".join(boardSpace[17]).center(cf(17))))
    print("|                 |                                                           "+fg(202)+"/            /"+ attr("reset")+"       |                 |")
    print("+--------+--------+                                                          "+fg(202)+"/   CHANCE   /"+ attr("reset")+"        +--------+--------+")
    print("|"+fg(70)+"Staff Common Room"+ attr("reset")+"|                                                         "+fg(202)+"/            /"+ attr("reset")+"         |       "+fg(208)+"S9"+ attr("reset")+"        |")
    print("|      $300       |                                                        "+fg(202)+"/            /"+ attr("reset")+"          |      $180       |")
    print("|{}|".format(" ".join(boardSpace[32]).center(cf(32))) + "                                                       "+fg(202)+"/            /"+ attr("reset")+"           |{}|".format(" ".join(boardSpace[18]).center(cf(18))))
    print("|{}|".format(housePrint(gameboard[32].level,"big"))+"                                                      "+fg(202)+"//////////////"+ attr("reset")+"            |{}|".format(housePrint(gameboard[18].level,"big")))
    print("+--------+--------+                                                                                +--------+--------+")
    print("| "+fg(70)+"Staff Bathrooms"+ attr("reset")+" |                                                                                |       "+fg(208)+"S12"+ attr("reset")+"       |")
    print("|      $300       |                                                                                |      $200       |")
    print("|{}|                                                                                |{}|".format(" ".join(boardSpace[31]).center(cf(31)), " ".join(boardSpace[19]).center(cf(19))))
    print("|{}|                                                                                |{}|".format(housePrint(gameboard[31].level,"big"), housePrint(gameboard[19].level,"big")))
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
    print("|    5 Demerits   |  "+fg(220)+"Drama"+ attr("reset")+" |   "+fg(146)+"IT"+ attr("reset")+"   |  "+fg(220)+"Music"+ attr("reset")+" |   "+fg(220)+"VA"+ attr("reset")+"   | "+fg(245)+"Fench."+ attr("reset")+" |"+fg(196)+"Library "+ attr("reset")+"| "+fg(196)+"Study"+ attr("reset")+"  |        |"+fg(196)+"Special"+ attr("reset")+" |  Staff Parking  |")
    print("|      _______    |  "+fg(220)+"Room"+ attr("reset")+"  |"+fg(146)+"HelpDesk"+ attr("reset")+"|  "+fg(220)+"Room"+ attr("reset")+"  |  "+fg(220)+"Room"+ attr("reset")+"  |"+fg(245)+"Station"+ attr("reset")+" |  "+fg(196)+"    "+ attr("reset")+"  |  "+fg(196)+"Room"+ attr("reset")+"  |        |  "+fg(196)+"Prov"+ attr("reset")+"  |    ______       |")
    print("|     / DIARY /,  |  $280  |  $150  |  $260  |  $260  |  $200  |  $240  |  $220  | CHANCE |  $220  |   /|_||_\`.__   |")
    print("|    /       //   |        |        |        |        |        |        |        |   ??   |        |  (   _    _ _\  |")
    print("|   /_______//    |        |        |        |        |        |        |        |        |        |  =`-(_)--(_)-'  |")
    print("|  (_______(/     |{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(" ".join(boardSpace[29]).center(sf(29)), " ".join(boardSpace[28]).center(sf(28)), " ".join(boardSpace[27]).center(sf(27)), " ".join(boardSpace[26]).center(sf(26)), " ".join(boardSpace[25]).center(sf(25)), " ".join(boardSpace[24]).center(sf(24)), " ".join(boardSpace[23]).center(sf(23)), " ".join(boardSpace[22]).center(sf(22)), " ".join(boardSpace[21]).center(sf(21)), " ".join(boardSpace[20]).center(cf(20))))
    print("|                 |{}|        |{}|{}|        |{}|{}|        |{}|                 |".format(housePrint(gameboard[29].level,"small"),housePrint(gameboard[27].level,"small"),housePrint(gameboard[26].level,"small"),housePrint(gameboard[24].level,"small"),housePrint(gameboard[23].level,"small"),housePrint(gameboard[21].level,"small")))
    print("+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+")
printBoard()
