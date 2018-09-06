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

class consumable(object):

    def __init__(self, choice):
        self.choice = choice

    def poop(self):
        if self.choice == "chance":
            print("pingers ;)")


gameboard = {}
with open("PropertyStats") as prop:
    for readin in prop:
        line = readin.split()
        if line[0] == "p":
            gameboard[line[2].replace("_", " ")] = PropertyCard(line[2].replace("_", " "), line[3].replace("_", " "), line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11])
        elif line[0] == "c":
            gameboard[line[2].replace("_", " ")] = consumable(line[2].replace("_", " "))
            pass


# print(gameboard["Mayfair"].colour)
