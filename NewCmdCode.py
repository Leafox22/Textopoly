from NewPropData import gameboard, properties, propset
import colored, sys, textwrap, time
from colored import stylize, fg, bg, attr
from VisualDice import show_dice
import random

print(attr("reset"))
playerlist = []

def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)

def num_check(feed):
    feed_input = input("{}{}".format(attr("reset"), feed))
    while type(feed_input) != int:
        try:
            feed_input = int(feed_input)
        except ValueError:
            feed_input = input("{}That's not even a valid number! Try another.\n\x1b[38;5;220m☞  ".format(attr("reset")))
    return feed_input

def cb():
    print("\n"*60) #cb = clear board ;)

def start_game():
    print("Welcome to Textopoly! Let's get started.\n")
    playnum = num_check("How many players are we having today?\n\x1b[38;5;220m☞  ")
    print(attr("reset"))
    while (playnum <= 1 or playnum > 4):
        if playnum == 1:
            playnum = num_check("You can't play Textopoly by yourself! How about another number?\n\x1b[38;5;220m☞  ")
            print(attr("reset"))
        if playnum > 4:
            playnum = num_check("Now that's quite the crowd, but I can only handle four at once, max. Another?\n\x1b[38;5;220m☞  ")
            print(attr("reset"))
        if playnum < 1:
            playnum = num_check("That doesn't sound right. How about another number?\n\x1b[38;5;220m☞  ")
            print(attr("reset"))
    print("Perfect! {} players. Now, what are your names?\n".format(playnum))
    for i in range(1, playnum+1):
        playname = input("{}Player {} name: \x1b[38;5;220m☞  ".format(attr("reset"), i))
        playerlist.append(player(playname))
    print(attr("reset"))
    print("Excellent. Now, pick a colour! This will show on property cards,\non the gameboard and on the menu.")
    colourray = [160, 208, 112, 121, 183, 126]
    for col in colourray:
        print(fg(col) + attr("bold") + "Colour: {}".format((colourray.index(col))+1))
    print()
    for i in playerlist:
        playcol = num_check("{}{}'s colour: \x1b[38;5;220m☞  ".format(attr("reset"), i.name))
        while (playcol > 7) or (playcol < 1):
            playcol = num_check("{}Choose a number listed above! \x1b[38;5;220m☞  ".format(attr("reset")))
        i.colour = colourray[playcol-1]
        i.colour_name()
    print(attr("reset"))
    print("Perfect. Final thing to do - you're each going to\nchoose a token for the gameboard.")
    tokenray = ["♘", "♖", "♧", "♡", "⚾︎", "♨︎"]
    print()
    for tok in tokenray:
        print("Token {}: {} ".format(tokenray.index(tok)+1, tok))
    print()
    for i in playerlist:
        playtok = num_check("{}{}'s token: \x1b[38;5;220m☞  ".format(attr("reset"), fg(i.colour) + attr("bold") + i.name + attr("reset")))
        while (playtok > 6) or (playtok < 1):
            playtok = num_check("{}Choose a number listed above! \x1b[38;5;220m☞  ".format(attr("reset")))
        i.token = tokenray[playtok-1]
    print(attr("reset"))
    print("And that's all we need for the setup!\nOn with the game!")
    print()
    playerlist[0].command_core()

class player(object):

    def __init__(self, name):
        self.name = name
        self.colour = ""
        self.money = 1500
        self.position = 0
        self.ownedprops = []
        self.token = ""
        self.hasrolled = False
        self.injail = False
        self.jailtime = 0
        self.lastroll = 0

    def colour_name(self):
        self.name = (fg(self.colour) + self.name + attr("reset"))
        self.token = (fg(self.colour) + self.token + attr("reset"))

    def command_core(self):
        com = input("{}What would you like to do?\n\x1b[38;5;220m☞  ".format(attr("reset"))).lower()
        cb()
        print(attr("reset"))
        if   (com == "roll")    or (com == "r"):
            self.roll()
        elif (com == "buy")     or (com == "b"):
            self.buy_prop()
        elif (com == "end")     or (com == "e"):
            if playerlist.index(self) != (len(playerlist) - 1):
                next = playerlist[playerlist.index(self)+1]
            else:
                next = playerlist[0]
            print("{}'s turn has ended, and it's {}'s turn to play!".format(self.name, next.name))
            self.hasrolled = False
            next.command_core()
        elif (com == "info")    or (com == "i"):
            gameboard[self.position].showcard()
            print()
            self.command_core()
        elif (com == "all")     or (com == "a"):
            self.prop_list()
        elif (com == "player")  or (com == "p"):
            self.inventory()
        elif (com == "upgrade") or (com == "u"):
            self.build()
        elif (com == "help") or (com == "?"):
            self.tooltips()
        else:
            print(textwrap.fill("Not a recognised command! Type [help] or [?] to see a list of all available commands.", 50))
            print()
            self.command_core()

    def tooltips(self):
        print('''
   _____   __         _________   ______      ______      _____
   ___  | / /_______________  /   ___  /_________  /_______ __ \\
   __   |/ /_  _ \  _ \  __  /    __  __ \  _ \_  /__ __ \_/ _/
   _  /|  / /  __/  __/ /_/ /     _  / / /  __/  / _ /_/ //_/
   /_/ |_/  \___/\___/\__,_/      /_/ /_/\___//_/   .___/(_)
                                                /_/
        ''')
        tippy = "help,    ? - show this card\nroll,    r - roll the dice and move player token\nbuy,     b - buy the tile the player's token is on\nend,     e - ends the current turn\ninfo,    i - display current tile's card\nall,     a - display list of properties in order to check stats\nplayer,  p - display current player's money and properties\nupgrade, u - build houses/hotels on owned properties"
        print(bordered(tippy))
        print()
        self.command_core()

    def roll(self):
        #roll cap
        if self.hasrolled == True:
            print("You've already rolled, {}! End the turn to roll again.".format(self.name))
            self.command_core()
        elif self.injail == True:
            self.prison_roll()
        #regular roll
        else:
            totalroll = roll1, roll2 = random.randint(1, 6), random.randint(1, 6)
            gopass, bonusroll = False, False
            show_dice(roll1, roll2)
            self.position += sum(totalroll)
            if self.position >= 40:
                self.position -= 40
                self.money += 200
                gopass = True
            print("{} is on {}.".format(self.name, gameboard[self.position].name))
            # if self.position
            if gopass is True:
                print("{} passed Go and collected $200!".format(self.name))
            self.hasrolled = True
            self.lastroll = sum(totalroll)
            self.quick_action()
            if roll1 == roll2:
                self.hasrolled = False
                print("{} rolled doubles, and gets a bonus roll!".format(self.name))
            self.command_core()
            return totalroll

    def prison_roll(self):
        if self.jailtime >= 3:
            print("The prisoner has served too long! {} must pay the $500 bail in order to leave.".format(self.name))
            paybail = input("Pay the $500 bail?\nBalance: ${}\n".format(self.money))
            if paybail.lower() == "yes" or "y":
                self.money -= 500
                self.injail = False
                print("That'll do. Now get out of here!\nBalance: ${}".format(self.money))
            else:
                print("Perhaps not yet then. Good luck doing anything from prison!")
        else:
            roll1, roll2 = random.randint(1, 6), random.randint(1, 6)
            show_dice(roll1, roll2)
            if roll1 == roll2:
                self.injail = False
                print("By sheer luck, {} is free! Next turn, the roll will count as a move.".format(self.name))
                self.jailtime = 0
            else:
                self.injail = True
                self.jailtime += 1
                print("No luck today. {} has served {} turn(s) in prison.".format(self.name, self.jailtime))
        self.hasrolled = True

    def quick_action(self):
        #property: paying rent and buying
        place = gameboard[self.position]
        if (
        (place.__class__.__name__ == "Property_Card")
        or (place.__class__.__name__ == "Railway") or (place.__class__.__name__ == "Utility")
        ):
            if (place.owner == None) and (self.money >= place.price):
                self.buy_prop()
            elif (place.owner != None):
                if place.owner != self:
                    print("{} is owned by {}.".format(place.name, place.owner.name))
                    if (place.__class__.__name__ == "Utility"):
                        utilcheck = 0
                        for look in place.owner.ownedprops:
                            if look.__class__.__name__ == "Utility":
                                utilcheck += 1
                        if utilcheck == 1:
                            mult = 4
                            utilrent = mult*(self.lastroll)
                        elif utilcheck == 2:
                            mult = 10
                            utilrent = mult*(self.lastroll)
                        if (self.money >= utilrent):
                            self.money -= utilrent
                            place.owner.money += utilrent
                            print("{} paid {} ${} rent ({} x ${}).\n".format(self.name, place.owner.name, utilrent, mult, self.lastroll))
                        elif (self.money < utilrent):
                            self.bankrupt(utilrent, place.owner)
                    elif (self.money >= place.rent[place.level]):
                        self.money -= place.rent[place.level]
                        place.owner.money += place.rent[place.level]
                        print("{} paid {} ${} rent.".format(self.name, place.owner.name, place.rent[place.level]))
                    elif (self.money < place.rent[place.level]):
                        self.bankrupt(place.rent[place.level], place.owner)
                    self.command_core()

    def buy_prop(self):
        place = gameboard[self.position]
        if (
        (place.__class__.__name__ == "Property_Card")
        or (place.__class__.__name__ == "Railway") or (place.__class__.__name__ == "Utility")
        ):
            if (place.owner == None) and (self.money >= place.price):
                buyreq = input("{} is unowned! Would you like to buy it for ${}?\n\x1b[38;5;220m☞  ".format(place.name, place.price)).lower()
                print(attr("reset"))
                if (buyreq == "info") or (buyreq == "i"):
                    place.showcard()
                    print()
                elif ("yes" in buyreq) or (buyreq == "y") or (buyreq == "buy") or (buyreq == "b"):
                        self.money -= place.price
                        place.owner = self
                        self.ownedprops.append(place)
                        print("{} now owns {}!\n".format(self.name, place.name))
                        self.command_core()
                else:
                    print("No? Maybe next time then.")
                    self.command_core()

            elif place.owner != None:
                print("{} already owns this property!".format(place.owner.name))
                self.command_core()
            elif self.money < place.price:
                print("Not enough money! {} costs ${} ({} has ${}).".format(place.name, place.price, self.name, self.money))
                self.command_core()
        else:
            print("You can't just buy {}!".format(place.name))
            self.command_core()

    def inventory(self):

        print('''
    ________                         _____                          ______
    ____  _/_________   _______________  /__________________  __    ___  /
     __  / __  __ \_ | / /  _ \_  __ \  __/  __ \_  ___/_  / / /    __  /
    __/ /  _  / / /_ |/ //  __/  / / / /_ / /_/ /  /   _  /_/ /      /_/
    /___/  /_/ /_/_____/ \___//_/ /_/\__/ \____//_/    _\__, /      (_)
                                                       /____/
        ''')
        # print("*" + "-"*49 + "*")
        # print("~ {}'s inventory ~".format(self.name).center(65))
        print("Balance    : ${}".format(self.money))
        print("Token      : {}".format(self.token))
        if len(self.ownedprops) > 0:
            stringy = self.ownedprops[0].name
        else:
            stringy = "-"
        for i in self.ownedprops[1:]:
            if len(self.ownedprops) > 1:
                stringy += ", " + i.name
        properties = "Properties : " + stringy
        print(textwrap.fill(properties, 100))
        print()
        print(">> To inspect owned properties sets, enter [i]")
        print("⇠  Or, press any other key to exit.")
        next = input("\x1b[38;5;220m☞ ")
        selectlist, count = [], 0
        if (next == "i") and (len(self.ownedprops) != 0):
            print(attr("reset"))
            colourdone = []
            for own in self.ownedprops:
                if own.colour not in colourdone:
                    for test in propset[own.colour]:
                        count += 1
                        if test in self.ownedprops:
                            print("[{}] ".format(count) + test.name + fg(own.colourpick(own.colour)) + " ✓" + attr("reset"))
                        else:
                            print("[{}] ".format(count) + attr("dim") + test.name + attr("reset"))
                        selectlist.append(test)
                    print()
                colourdone.append(own.colour)
            ind = input("    Property to inspect (press a key not listed above to exit)\n    \x1b[38;5;220m☞  ").lower()
            cb()
            try:
                if int(ind) in range(1, len(selectlist)+1):
                    print(attr("reset"))
                    selectlist[int(ind)-1].showcard()
                    print()
                    self.command_core()
                else:
                    self.command_core()
            except ValueError:
                self.command_core()
        elif (next == "i") and (len(self.ownedprops) == 0):
            print(attr("reset"), attr(1), attr(2))
            print(textwrap.fill("Look, we appreciate the passion for inspection but you don't currently have any properties to look at! Come back when you're a true real estate mogul.", 51))
            print(attr("reset") + "*" + "-"*49 + "*")
            print()
            self.command_core()
        else:
            cb()
            self.command_core()

    def prop_list(self):
        print(attr("reset"))
        print('''
  ________                                 _____
  ___  __ \__________________________________  /_____  __
  __  /_/ /_  ___/  __ \__  __ \  _ \_  ___/  __/_  / / /
  _  ____/_  /   / /_/ /_  /_/ /  __/  /   / /_ _  /_/ /
  /_/     /_/    \____/_  .___/\___//_/    \__/ _\__, /
                     /_/                      /____/
  ______  ___                           ______   ______
  ___   |/  /_____ ___________  _______ ___  /   ___  /
  __  /|_/ /_  __ `/_  __ \  / / /  __ `/_  /    __  /
  _  /  / / / /_/ /_  / / / /_/ // /_/ /_  /      /_/
  /_/  /_/  \__,_/ /_/ /_/\__,_/ \__,_/ /_/      (_)
        ''')
        print(bordered("|  OWNER  |        PROPERTY        |  BUILD LVL  |"))
        counter = 0
        biglist = []
        for i in gameboard:
            if i.__class__.__name__ == "Property_Card":
                biglist.append(i)
                counter += 1
                if len(str(i.colourpick(i.colour))) < 3:
                    j = 39
                elif len(str(i.colourpick(i.colour))) == 3:
                    j = 40
                if i.owner == None:
                    print(" |" + ("-").center(9) + "|  " + i.name.ljust(j) + " |  ", end="")
                    if i.level < 5:
                        print((("✧ "*i.level) + ("  "*(5 - i.level))).ljust(11) + "|" + " [{}]".format(counter))
                    elif i.level == 5:
                        print("✦ "*5 + " |" + " [{}]".format(counter))
                elif i.owner != None:
                    print(" |" + (fg(i.owner.colour) + i.owner.token + attr("reset")).center(39) + "|  " + i.name.ljust(j) + " |  ", end="")
                    if i.level < 5:
                        print((("✧ "*i.level) + ("  "*(5 - i.level))).ljust(11) + "|" + " [{}]".format(counter))
                    elif i.level == 5:
                        print("✦ "*5 + " |" + " [{}]".format(counter))
        print(" +" + "-"*48 + "+")
        for i in gameboard:
            if i.__class__.__name__ == "Railway":
                biglist.append(i)
                counter += 1
                if i.owner == None:
                    print(" |" + ("-").center(9) + "|  " + i.name.ljust(40) + " |  " + "   N/A     | [{}]".format(counter))
                elif i.owner != None:
                    print(" |" + (fg(i.owner.colour) + i.owner.token + attr("reset")).center(39) + "|  " + i.name.ljust(40) + " |  " + "   N/A     | [{}]".format(counter))
        print(" +" + "-"*48 + "+")
        for i in gameboard:
            if i.__class__.__name__ == "Utility":
                biglist.append(i)
                counter += 1
                if i.owner == None:
                    print(" |" + ("-").center(9) + "|  " + i.name.ljust(40) + " |  " + "   N/A     | [{}]".format(counter))
                elif i.owner != None:
                    print(" |" + (fg(i.owner.colour) + i.owner.token + attr("reset")).center(39) + "|  " + i.name.ljust(40) + " |  " + "   N/A     | [{}]".format(counter))
        print(" +" + "-"*48 + "+")
        # print(biglist[counter-1].name)
        print()
        ind = input("{}  Property to inspect (press a key not listed above to exit)\n  \x1b[38;5;220m☞  ".format(attr("reset"))).lower()
        cb()
        try:
            if int(ind) in range(1, 29):
                print(attr("reset"))
                biglist[int(ind)-1].showcard()
                print()
                self.command_core()
            else:
                print()
                self.command_core()
        except ValueError:
            print()
            self.command_core()

    def build(self):

        maybelist, upglist, count, keepgo, upgradeprop = [], [], 0, True, True
        print(attr("reset"), attr("bold"))
        print("""
    _____  __                             _________                ______
    __  / / /______________ _____________ ______  /____________    ___  /
    _  / / /___  __ \_  __ `/_  ___/  __ `/  __  /_  _ \_  ___/    __  /
    / /_/ / __  /_/ /  /_/ /_  /   / /_/ // /_/ / /  __/(__  )      /_/
    \____/  _  .___/_\__, / /_/    \__,_/ \__,_/  \___//____/      (_)
            /_/     /____/
               """)
        colourdone = []
        for own in self.ownedprops:
            if own.colour not in colourdone:
                if own.__class__.__name__ == "Property_Card":
                    keepgo = True
                    for test in propset[own.colour]:
                        if (test in self.ownedprops) and (keepgo == True):
                            maybelist.append(test)
                        else:
                            maybelist = []
                            keepgo = False
                    if maybelist != []:
                        for yeslist in maybelist:
                            count += 1
                            if yeslist.level < 5:
                                print("{}[{}] ".format(attr("reset"), count) + yeslist.name + fg(own.colourpick(own.colour)) + " " +(yeslist.level * "✧") + attr("reset"))
                            else:
                                print("{}[{}] ".format(attr("reset"), count) + yeslist.name + fg(own.colourpick(own.colour)) + " " +(5 * "✦") + attr("reset"))
                            upglist.append(yeslist)
                        maybelist = []
                print()
            colourdone.append(own.colour)
        if len(upglist) == 0:
            print("{}{}Sorry pal, but you don't own any full sets of properties. Keep buyin' big and you'll \nwin bigger! Check your player screen to see how close you're getting if you'd like.".format(attr(1), attr(2)))
            upgradeprop = False
            print()
            self.command_core()
        try:
            while upgradeprop == True:
                ind = input("    Property to upgrade (press a key not listed above to exit)\n    \x1b[38;5;220m☞  ").lower()
                print()
                curr = upglist[int(ind)-1]
                if int(ind)-1 < 0:
                    raise IndexError
                print(attr("reset"))
                if curr.level < 5:
                    curr.showcard()
                    print()
                    upgcheck = input("    Building upon this property will cost ${} and will increase the rent gained to ${}. Would you like to do so? \n    \x1b[38;5;220m☞  ".format(curr.buildprice, curr.rent[curr.level+1])).lower()
                    print(attr("reset"))
                    if ("yes" in upgcheck) or (upgcheck == "y") or (upgcheck == "buy") or (upgcheck == "b"):
                        if self.money >= curr.buildprice:
                            self.money -= curr.buildprice
                            curr.level += 1
                            upgradeprop = False
                            print("    {} is now on level {}! Pleasure doing business with ya.\n".format(curr.name, curr.level))
                            self.command_core()
                        elif self.money < curr.buildprice:
                            print("{}{}    You don't have enough cash for that! Come back when you have the dough bro.{}".format(attr("dim"), attr("bold"), attr("reset")))
                    else:
                        print("{}{}    What a shame. If you'd like to head up any more construction, we'll be here!{}".format(attr("dim"), attr("bold"), attr("reset")))
                        print()
                else:
                    print("    {}{}This property is already fully developed! You're raking in the most you can, pal.".format(attr("dim"), attr("bold")))
                    print(attr("reset"))
            # else:
            #     print(attr("reset") + "*" + "-"*49 + "*")
            #     self.command_core()
        except (IndexError, ValueError):
            cb()
            self.command_core()

    def bankrupt(self, rentowed, owee):
        print("\nUh oh. {} owes {} ${} rent, but only has ${}!".format(self.name, owee.name, rentowed, self.money))
        time.sleep(3)
        print("""

        ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗███████╗    ██████╗  ██████╗ ██╗  ██╗██╗   ██╗███████╗    ██████╗ ██╗████████╗ ██████╗██╗  ██╗
        ██╔══██╗██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔════╝    ██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔════╝    ██╔══██╗██║╚══██╔══╝██╔════╝██║  ██║
        ██████╔╝██████╔╝██║   ██║█████╔╝ ██║   ██║███████╗    ██████╔╝██║   ██║█████╔╝ ██║   ██║███████╗    ██████╔╝██║   ██║   ██║     ███████║
        ██╔══██╗██╔══██╗██║   ██║██╔═██╗ ██║   ██║╚════██║    ██╔═══╝ ██║   ██║██╔═██╗ ██║   ██║╚════██║    ██╔══██╗██║   ██║   ██║     ██╔══██║
        ██████╔╝██║  ██║╚██████╔╝██║  ██╗╚██████╔╝███████║    ██║     ╚██████╔╝██║  ██╗╚██████╔╝███████║    ██████╔╝██║   ██║   ╚██████╗██║  ██║
        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═════╝ ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝


""")

# ✧✦



# start_game()

# # P1 INITIALISATION
# playerlist.append(player("Tim"))
# playerlist[0].colour = 123
# playerlist[0].money = 5
# playerlist[0].token = "♘"
# playerlist[0].colour_name()
# playerlist[0].position = 5
#
# # ADDING PROPERTIES TO P1
# playerlist[0].ownedprops.append(gameboard[39])
# gameboard[39].owner = playerlist[0]
# gameboard[39].level = 5
# playerlist[0].ownedprops.append(gameboard[5])
# gameboard[5].owner = playerlist[0]
# playerlist[0].ownedprops.append(gameboard[34])
# gameboard[34].owner = playerlist[0]
# playerlist[0].ownedprops.append(gameboard[37])
# gameboard[37].owner = playerlist[0]
# #
# # # P2 INITIALISATION
# playerlist.append(player("Lachlan"))
# playerlist[1].colour = 160
# playerlist[1].token = "♖"
# playerlist[1].colour_name()
#
# playerlist[1].ownedprops.append(gameboard[12])
# gameboard[12].owner = playerlist[1]
# playerlist[1].ownedprops.append(gameboard[28])
# gameboard[28].owner = playerlist[1]
#
# playerlist[0].command_core()

# RENT TEST
'''
playerlist[0].ownedprops[0].level = 5
playerlist[0].ownedprops[0].showcard()
playerlist[0].position = 12
gameboard[9].owner = playerlist[0]
playerlist[1].roll()
'''
