from pantry import Ingredients

i = Ingredients()
dhal = i.add("Toor Dhal", "1.5", "cup")
tomatoes = i.add("Ripe Tomatoes", "3")
cumin = i.add("Cumin seeds", "1", "tablespoon")
cocnut = i.add("Grated coconut", "0.5", "cup")
chillies = i.add("Green chilli peppers", "8")

i.printall()