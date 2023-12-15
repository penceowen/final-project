from random import randint

thisdict0 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1 = {
  "brand": "Toyota",
  "model": "Prius",
  "year": 2019
}
thisdict2 = {
  "brand": "Honda",
  "model": "Civic Si",
  "year": 2018
}
thisdict3 = {
  "brand": "Tesla",
  "model": "S",
  "year": 2022
}

# creates list containers
proteins = []
vegetables = []
carbs = []

# this populates the lists with dictionaries
proteins.append(thisdict0)
proteins.append(thisdict1)
proteins.append(thisdict2)
proteins.append(thisdict3)

# this random selects and prints
print(proteins[randint(0,3)])