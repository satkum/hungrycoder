class Ingredient(object):
    def __init__(self, name, quantity, units):
        self.name = name
        self.quantity = quantity
        self.units = units

    def __unicode__(self):
        return self.name

    def printitem(self):
        print "{0} - {1} {2}".format(self.name, self.quantity, self.units)

class Ingredients(object):
    ingredients = []

    def add(self, item, quantity, units="Nos"):
        ingredient = Ingredient(item, quantity, units)
        self.ingredients.append(ingredient)
        return ingredient

    def printall(self):
        print "List of ingredients:\n"
        for i in self.ingredients:
            i.printitem()