# This was created by: Owen Pence



# This category is the protein options

thisdict0 = {
    "food": "salmon",
    "category": "protein",
    "calories": "1200"
}
chicken = {
  "calories": "1500",
  "category": "protein", 
}
turkey = {
  "calories": 1000,
  "category": "protein",
}
beef = {
  "calories": 2500,
  "category": "protein",
}
pork = {
  "calories": 900,
  "category": "protein",
}
# This category is the carbohydrates options

bread = {
     "calories": 1000,
    "category": "carbohydrate",
}
rice = {
     "calories": 400,
    "category": "carbohydrate",
},
potatoes = {
     "calories": 600,
    "category": "carbohydrate",
},
beans= {
     "calories": 600,
    "category": "carbohydrate",
},
pasta = {
     "calories": 2000,
    "category": "carbohydrate",
},
# This category contains the data for the vegetable options 

carrot = {
     "calories": 1000,
    "category": "vegetable",
}
cucumber= {
     "calories": 700,
    "category": "vegetable",
},
peas = {
     "calories": 250,
    "category": "vegetable",
},
greenbeans = {
     "calories": 300,
    "category": "vegetable",
},
corn = {
     "calories": 800,
    "category": "vegetable",
},


from random import randint
# This date contains the 5 protein foods with their calories
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

thisdict5 = {
  "category": "carbohydrates",
  "food": "bread",
  "calories": 1964
}
thisdict6 = {
  "category": "proteins",
  "model": "chicken",
  "calories": 2019
}
thisdict7 = {
  "category": "proteins",
  "model": "turkey",
  "calories": 2018
}
thisdict8 = {
  "category": "proteins",
  "model": "beef",
  "calories": 2022
}
thisdict9 = {
  "category": "proteins",
  "model": "pork",
  "calories": 2022
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
print(proteins[randint(0,4)]carbohydrates[randint(5,9)])

