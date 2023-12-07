# This was created by: Owen Pence



# This category is the protein options

salmon = {
     "calories": 1200,
    "category": "protein",
}
chicken = {
  "calories": 1500,
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



print(category["protein"])

meal = []

meal.append(chicken["category"])
meal.append(chicken["category"])
meal.append(chicken["category"])
meal.append(chicken["category"])
meal.append(Salmon["category"])

print(meal)

proteins = 0

for i in meal:
    print(i)
    if i == "protein":
        proteins += 1

print(proteins)