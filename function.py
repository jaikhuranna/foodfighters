import pandas as pd
import random
import json

def jsontolist(a):
    f = open(str(a))
    l = json.load(f)
    al = list(l.values())
    al
    for i in range(len(al)):
        al[i] = int(al[i])
    return al

df = pd.read_csv("/home/jaikhurana/Documents/Projects/foodfighters/Dataset/dummydataset.csv")

f = open('data.json')
l = json.load(f)

def mainfun(filename):
    
    al = jsontolist(filename)
    
    valid = (1,2,3,4,5,6)

    ingiq = al[0]
    dis = al[1]

    if ingiq == 1:
        ingiq = ingiq+1
    
    if dis not in valid:
        print("ERROR: invalid response")
    if ingiq not in valid:
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
    if len(l) == 0:
        return 'no'
    else:
        ans = l[random.randint(0, len(l))]
        return ans

print(mainfun('data.json'))