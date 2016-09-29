class Ingredient(object):
    def __init__(self, name, quantity, units):
        self.name = name
        self.quantity = quantity
        self.units = units

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

    def printSelf(self):
        print "{0} - {1} {2}".format(self.name, self.quantity, self.units)

class Ingredients(object):
    ingredients = []

    @classmethod
    def add(cls,item, quantity, units="Nos"):
        ingredient = Ingredient(item, quantity, units)
        cls.ingredients.append(ingredient)
        return ingredient

    @classmethod
    def acquireAll(cls):
        print "List of ingredients:"
        for i in cls.ingredients:
            i.printSelf()
        print "\n"
