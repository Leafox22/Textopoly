import textwrap
from colored import fg, attr, stylize

def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)

class Property_Card:

    def __init__(self, name, colour, price, rent, onehouse, twohouse, threehouse, fourhouse, hotel, buildprice):
        self.nametext = name
        self.name = (fg(self.colourpick(colour)) + attr("bold") + name + attr("reset"))
        self.colour = colour
        self.price = int(price)
        self.rent = [int(rent), int(onehouse), int(twohouse), int(threehouse), int(fourhouse), int(hotel)]
        self.level = 0
        self.buildprice = int(buildprice)
        self.owner = None

    def colourpick(self, colour):
        colourio = {
        "brown" : 94,
        "light blue" : 159,
        "pink" : 201,
        "orange" : 208,
        "red" : 196,
        "yellow" : 220,
        "green" : 70,
        "dark blue" : 20
        }
        return colourio[colour]

    def showcard(self):
        print("*-----------------------------*")
        print(self.name.center(50))
        if (self.level < 5) and (self.level >= 1):
            print(("✧ "*self.level).center(30))
        elif self.level == 5:
            print(("✦ "*5).center(30))
        printable = str("           ~${}~\nRent with no buildings: ${} \n    \"        one house: ${}\n    \"       two houses: ${}\n    \"     three houses: ${}\n    \"      four houses: ${}\n    \"            hotel: ${}").format(self.price, self.rent[0], self.rent[1], self.rent[2], self.rent[3], self.rent[4], self.rent[5])
        print(bordered(printable))
        print("${} to build".format(self.buildprice).center(31))
        if self.owner != None:
            print("< Owned by {} >".format(self.owner.name).center(48))
        print("*-----------------------------*")

    def charge_rent(self):
        return 15

class Not_Prop:

    def showcard(self):
        if self.__class__.__name__.lower().replace("_", " ") != "railway":
            print("*-------------------------------------*")
            if self.__class__.__name__.lower() == "utility":
                print(" {} ".format(self.name.center(56)))
            else:
                print(" {} ".format(self.name.center(35)))
            if not (self.name == "Community Chest" or self.name == "Chance" or self.__class__.__name__.lower() == "othertile" or self.name == "Jail"):
                print(" - {} - ".format(self.__class__.__name__.lower().replace("_", " ")).center(38))
            print(bordered(textwrap.fill(self.info, 36)))
            print("*-------------------------------------*")
        elif self.__class__.__name__.lower().replace("_", " ") == "railway":
            print("*----------------------------*")
            print(" {} ".format(self.nametext.center(26)))
            printy = fg(245) + attr("bold") + "- Railway -" + attr("reset")
            print(printy.center(48))
            print(bordered("Rent with one railway: $25\n    \"    two railways: $50\n    \"  three railways: $100\n    \"   four railways: $200"))
            if self.owner != None:
                print("< Owned by {} >".format(self.owner.name).center(42))
            print("*----------------------------*")

class Chance_Card(Not_Prop):

    def __init__(self):
        self.name = "Chance"
        self.info = "When you land here, use the \"draw\" command to pick a card! Most of the chance cards will move you to a new space on the board, but some will pay you money."

    def drawcard(self):
        pass
        # when filled, will randomly select a function from a list.

class Community_Chest(Not_Prop):

    def __init__(self):
        self.name = "Community Chest"
        self.info = "When you land here, use the \"draw\" command to pick a card! Most of the community chest cards will pay you some money, but others may cost you something..."

    def drawcard(self):
        pass
        # when filled, will randomly select a function from a list.

class Railway(Not_Prop):

    def __init__(self, name):
        self.nametext = name
        self.name = (fg(245) + attr("bold") + name + attr("reset"))
        self.price = 200
        self.rent = [25, 50, 100, 200]
        self.level = 0

        self.owner = None

class OtherTile(Not_Prop):

    def __init__(self, name):
        self.name = name
        if name == "Go":
            self.info = "The starting tile of the board. Pass here and get $200!"
        if name == "Income Tax":
            self.rent = 200
            self.info = "You didn't think you'd keep all this money you're earning did you? Pay $200 or 10% of everything you own!"
        if name == "Super Tax":
            self.rent = 75
            self.info = "Living is expensive, and so is insurance! Landing here means you have to pay $75. Not quite as much as income tax!"
        if name == "Go To Jail":
            self.info = "How are you reading this? The source code is off limits! You should ACTUALLY go to jail."
        if name == "Free Parking":
            self.info = "You lucky duck! If you've landed here, it means you've collected all of the taxes anyone has paid. Enjoy the free cash!"
            self.stash = 0      # This is where the tax goes so you can claim it by landing!

    def taxcalc(self):
        pass

class Jail(Not_Prop):

    def __init__(self, name):
        self.name = name
        self.info = "This is where you go if you've been sent here by an unlucky tile, an unfortunate chance card, or speeding. If you're stuck in here, you can get out by:                1) paying $500 bail,                    2) redeeming the necessary card,           3) rolling doubles.               After 3 unsuccessful roll attempts, the bail must be paid anyway and the player is free to go."

class Utility(Not_Prop):

    def __init__(self, name):
        self.nametext = name
        self.name = (fg(146) + attr("bold") + name + attr("reset"))
        self.price = 150
        self.info = "If ONE Utility is owned, rent is 4x amount shown on dice.\nIf BOTH Utilities are owned, rent is 10x the amount shown on the dice."
        self.owner = None

# class ToDo:           # Don't delete just yet! This just acts
#                               # as a filler for anything we haven't
#     def __init__(self):       # done yet. If we delete stuff/work
#         self.name = "---"     # backwards, we'll need it again.

def boardcreate():
    properties = {}
    go = OtherTile("Go")
    gameboard = []
    with open("PropertyStats") as prop:
        for readin in prop:
            line = readin.split()
            if line[0] == "p":
                properties[line[2].replace("_", " ")] = Property_Card(line[2].replace("_", " "), line[3].replace("_", " "), line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11])
                gameboard.append(properties[line[2].replace("_", " ")])
            elif line[0] == "cc":
                gameboard.append(Community_Chest())
            elif line[0] == "?":
                gameboard.append(Chance_Card())
            elif line[0] == "r":
                gameboard.append(Railway(line[2].replace("_", " ")))
            elif line[0] == "j":
                gameboard.append(Jail(line[2].replace("_", " ")))
            elif line[0] == "u":
                gameboard.append(Utility(line[2].replace("_", " ")))
            elif line[0] == "o":
                gameboard.append(OtherTile(line[2].replace("_", " ")))
            else:
                gameboard.append(ToDo())
    return gameboard, properties

gameboard, properties = boardcreate()[0], boardcreate()[1]


'''
Here's an introductory lesson on classes that explains stuff better than I ever could (text):
https://www.digitalocean.com/community/tutorials/how-to-construct-classes-and-define-objects-in-python-3
'''
