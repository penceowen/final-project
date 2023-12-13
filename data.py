# This was created by: Owen Pence



# This category is the protein options

# This category is the carbohydrates options

# This category contains the data for the vegetable options 



from random import randint
# This list contains the 5 protein foods with their calories
thisdict0 = {
  "category": "proteins",
  "food": "salmon",
  "calories": 1964
}
thisdict1 = {
  "category": "proteins",
  "model": "chicken",
  "calories": 2019
}
thisdict2 = {
  "category": "proteins",
  "model": "turkey",
  "calories": 2018
}
thisdict3 = {
  "category": "proteins",
  "model": "beef",
  "calories": 2022
}
thisdict4 = {
  "category": "proteins",
  "model": "pork",
  "calories": 2022
}

# This list contains the 5 protein foods with their calories
thisdict5 = {
  "category": "carbohydrates",
  "food": "bread",
  "calories": 1000
}
thisdict6 = {
  "category": "carbohydrates",
  "model": "rice",
  "calories": 400
}
thisdict7 = {
  "category": "carbohydrates",
  "model": "potatoes",
  "calories": 600 
}
thisdict8 = {
  "category": "carbohydrates",
  "model": "beans",
  "calories": 600
}
thisdict9 = {
  "category": "carbohydrates",
  "model": "pasta",
  "calories": 2000
}

# This list contains the 5 vegetable options listed in their category with the amount of calories they contain
thisdict10 = {
  "category": "vegetables",
  "food": "carrot",
  "calories": 1000
}
thisdict11 = {
  "category": "vegetables",
  "model": "cucumber",
  "calories": 700
}
thisdict12 = {
  "category": "vegetables",
  "model": "peas",
  "calories": 250 
}
thisdict13 = {
  "category": "vegetables",
  "model": "greenbeans",
  "calories": 300
}
thisdict14= {
  "category": "vegetabes",
  "model": "corn",
  "calories": 800
}

# creates list containers
proteins = []
vegetables = []
carbohydrates = []

# this populates the lists with dictionaries
proteins.append(thisdict0)
proteins.append(thisdict1)
proteins.append(thisdict2)
proteins.append(thisdict3)
proteins.append(thisdict4)

carbohydrates.append(thisdict5)
carbohydrates.append(thisdict6)
carbohydrates.append(thisdict7)
carbohydrates.append(thisdict8)
carbohydrates.append(thisdict9)

vegetables.append(thisdict10)
vegetables.append(thisdict11)
vegetables.append(thisdict12)
vegetables.append(thisdict13)
vegetables.append(thisdict14)



# this random selects and prints
print(proteins[randint(0,4)])
print(carbohydrates[randint(0,4)])
print(vegetables[randint(0,4)])