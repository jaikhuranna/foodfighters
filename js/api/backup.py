
from flask import Flask, jsonify, request
import pandas as pd
import random
import json

app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    return "Welcome to our hell2U!"
# GET request 




@app.route('/getmsg/', methods=['GET'])
def get_message():
    return jsonify({'message': 'This is a GET request'})








# POST request
@app.route('/postmsg/', methods=['POST'])
def mainfun():
    if request.method == "POST":
        df = pd.read_csv("/var/www/html/FoodFighters/api/foodfighters/Dataset/dummydataset.csv")
        message = request.get_json(force=True)
        # f = open(str(message))
        # l = json.load(message)
        # al = list(l.values())
        # for i in range(len(al)):
        #     al[i] = int(al[i])
        
        ingiq = int(message["ingredients"])
        dis = int(message["disease"])
        

        if ingiq == 1:
            ingiq = ingiq+1

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
            return jsonify({'Recipe': ans})
            
    # return jsonify({'Recipe': ans})ss
    # return jsonify({'num1': num1,"num2":num2})












































if __name__ == '__main__':
    app.run()
    