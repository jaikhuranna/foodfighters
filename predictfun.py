import pandas as pd
import random
df = pd.read_csv("/home/jaikhurana/Documents/Projects/foodfighters/Model/Dataset/dummydataset.csv")

valid = (1,2,3,4,5,6)
ingiq = int(input("Enter the Ingredient in question:\n1. Meat\n2. Rice\n3. Milk\n4. Sugar\n5. Wheat\n6. Soy\nYour Answer: "))

if ingiq not in valid:
    print("ERROR: invalid response")

dis = int(input("Enter the Disease\n1. obesity \n2. diabetes \n3. cardiovascular disease \n4. cancer \n5. dental disease \n6. osteoporosis\nYour answer: "))

if dis not in valid:
    print("ERROR: invalid response")

    # checking for diseases
#conditions

if dis == 1:
    discon = "Fat < 50 and Carbs < 57"
elif dis == 2:
    discon = "Fat < 50 and Carbs < 57"
elif dis == 3:
    discon = "Fat < 50"
elif dis == 4:
    discon = "Protein > 50"
elif dis == 5:
    discon = "Carbs < 57 and Protein > 50"
elif dis == 6:
    discon = "Protein > 50"

    #checking for ingredients in question
#conditions
fish = [Sablefish
Salmon,Sardines ,Scallop,Scorpion Fish,Sea Trout,Shad 
Shark
Shrimp
Snapper
Sole
Spanish Mackerel
Squid 
calamari 
Swordfish
Tilapia
Tilefish 
Tuna 
Walleye 
Weakfish
White Croaker 
Whitefish
Whiting
Anchovy
Bass 
Bluefish
Buffalo Fish
Butterfish
Carp
Catfish 
Chilean sea bass
Clam
Cod
Crab 
Crayfish 
Croaker 
Flounder
Golden Snapper
Grouper
Haddock
Hake
Halibut
Herring 
Jack 
Jacksmelt
King Mackerel
Lobster 
Mackerel 
Mahi Mahi 
Marlin
Mullet
Orange Roughy
Oysters 
Perch 
Pickerel
Plaice
Pollock
Pompano 
Rainbow Trout]

if ingiq == 1:
    ingcon = "\" + 
if ingiq == 2:
    ingcon = "Carbs < 59"
if ingiq == 3:
    ingcon = "Fat > 54"
if ingiq == 4:
    ingcon = "Carbs > 59"
if ingiq == 5:
    ingcon = "Carbs > 59"
if ingiq == 6:
    ingcon = "Protein > 54"

condition = str(ingcon + " and " + discon)

set = df.query(condition)
l = list(set["Recipe_name"])
ans = l[random.randint(0, len(l))]
print(ans)