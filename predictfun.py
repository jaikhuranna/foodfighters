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


if ingiq == 1:
    ingcon = "\Salmon or \Sardines or \lamb or \meat or \chicken or \pork or \mutton or \lamb" 
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
if ans == "":
    print("haha")
else:
    print(ans)