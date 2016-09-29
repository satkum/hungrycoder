from utils.pantry import Ingredients
from utils.cookingMethods import *

oil = Ingredients.add("Vegetable oil", "2", "tablespoon")
dhal = Ingredients.add("Toor dhal", "1.5", "cup")
salt = Ingredients.add("Salt", "to taste", "")
cumin = Ingredients.add("Cumin seeds", "1", "tablespoon")
coconut = Ingredients.add("Grated coconut", "0.5", "cup")
chillies = Ingredients.add("Green chilli peppers", "8")
tomatoes = Ingredients.add("Ripe tomatoes", "3")
turmeric = Ingredients.add("Turmeric powder", "0.25", "tespoon")
asafoetida = Ingredients.add("Asafoetida powder", "0.25", "teaspoon")
#Cut the vegetable in small cubes, can use cabbage instead
vegetable = Ingredients.add("Squash", "1")
#For final tempering
channaDhal = Ingredients.add("Channa dhal", "2", "teaspoon")
curryLeaves = Ingredients.add("Curry leaves", "5")
mustard = Ingredients.add("Mustard seeds", "1", "teaspoon")

Ingredients.acquireAll()

#Use water to dhal ratio of 1:2
cookedMixture = cook(dhal,tomatoes,turmeric,oil)
simmeringMixture = simmer(cookedMixture)

simmeringMixture = add(simmeringMixture, vegetable, salt)

cumin = fry(cumin)
blendedMixture = blend(cumin, chillies, coconut)
simmeringMixture = add(simmeringMixture, blendedMixture)

temperMix = temper(mustard, channaDhal, curryLeaves, asafoetida)
simmeringMixture = add(simmeringMixture, temperMix)