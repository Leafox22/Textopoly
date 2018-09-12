class PropertyCard(object):

    def __init__(self, name, colour, price, rent, onehouse, twohouse, threehouse, fourhouse, hotel, buildprice, *owner):
        self.name = name
        self.colour = colour
        self.price = price
        self.rent = rent
        self.onehouse = onehouse
        self.twohouse = twohouse
        self.threehouse = threehouse
        self.fourhouse = fourhouse
        self.hotel = hotel
        self.buildprice = buildprice
        self.owner = owner

class ChanceCard(object):

    def __init__(self):
        self.name = "Chance"

    def drawcard(self):
        pass
        # when filled, will randomly select a function from a list.

class CmuChest(object):

    def __init__(self):
        self.name = "Community Chest"

    def drawcard(self):
        pass
        # when filled, will randomly select a function from a list.

class railway(object):

    def __init__(self, name):
        self.name = name
        self.price = 200
        self.rent1 = 25
        self.rent2 = 50
        self.rent3 = 100
        self.rent4 = 200

class OtherTile(object):

    def __init__(self, name):
        self.name = name
        if name == "Go":
            self.info = "The starting tile of the board. Pass here and get $200!"
        if name == "Income Tax":
            self.rent = 200
        if name == "Super Tax":
            self.rent = 75
        if name == "Jail":
            pass
        if name == "Go To Jail":
            pass
        if name == "Free Parking":
            self.stash = 0      # This is where the tax goes so you can claim it by landing!

    def taxcalc(self):
        pass

class Utility(object):

    def __init__(self, name):
        self.name = name
        self.price = 150

# class ToDo(object):           # Don't delete just yet! This just acts
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
                properties[line[2].replace("_", " ")] = PropertyCard(line[2].replace("_", " "), line[3].replace("_", " "), line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11])
                gameboard.append(properties[line[2].replace("_", " ")])
            elif line[0] == "cc":
                gameboard.append(CmuChest())
            elif line[0] == "?":
                gameboard.append(ChanceCard())
            elif line[0] == "r":
                gameboard.append(railway(line[2].replace("_", " ")))
            elif line[0] == "o":
                gameboard.append(OtherTile(line[2].replace("_", " ")))
            elif line[0] == "u":
                gameboard.append(Utility(line[2].replace("_", " ")))
            else:
                gameboard.append(ToDo())
    return gameboard, properties

# gameboard, properties = boardcreate()[0], boardcreate()[1]         # boardcreate() returns gameboard
# for i in gameboard:                                                # and properties, it creates the
#     print(i.name)                                                  # board once it's run. Pretty cool.
