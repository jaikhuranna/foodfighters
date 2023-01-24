import pandas as pd
ds = pd.read_csv('/home/jaikhurana/Documents/Projects/foodfighters/Model/Dataset/dummydataset.csv')


ingiq = input("Enter the Ingredient in question: ")
dis = int(input("1. obesity \n2. diabetes \n3. cardiovascular disease \n4. cancer \n5. dental disease \n6. osteoporosis\nYour answer: "))
valid = (1,2,3,4,5,6)

if dis not in valid:
    print("ERROR: invalid response")
print(ds)

"""
obesity- Low fat(33g-50g), low carbs(20g-57g)
diabetes - Low fat(33g-50g), low carbs(20g-57g)
cardiovascular disease - Low fat(33g-50g)
cancer - 50-175g high protein
dental disease - low carbs(20g-57g), high protein
osteoporosis - high protein 
"""
