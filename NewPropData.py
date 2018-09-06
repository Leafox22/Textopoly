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

a = PropertyCard("Old Kent Rd", "brown", "60", "2", "10", "30", "90", "160", "250", "50")
