# import requests
from flask import Flask,render_template, request
import pickle

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
def load_model():
    try:
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
    except FileNotFoundError:
        raise Exception("model.pkl not found in project root")
    return model

@app.route('/predict',methods=['POST','GET'])
def predict():
    # if request.method=='POST':
    #     age=int()
    model=load_model()
    user_input=request.form.get('temperature')
    prediction=model.predict([[int(user_input)]])
    prediction=round(prediction[0],2)
    print(prediction)
    return render_template('index.html',prediction_text=f"The total revenue generted is ${prediction}")

if __name__ =="__main__":
    app.run(debug=True)