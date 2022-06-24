from flask import Flask, request, render_template
import pickle as pkl

app= Flask(__name__)

model=pkl.load(open('model.pkl','rb'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    Nitrogen=int(request.form['Nitrogen'])
    Phosphorous=int(request.form['Phosphorous'])
    Potassium=int(request.form['Potassium'])
    Temperature=float(request.form['Temperature'])
    Humidity=float(request.form['Humidity'])
    pH=float(request.form['pH'])
    Rainfall=float(request.form['rainfall'])
    predicted=model.predict([[Nitrogen, Phosphorous, Potassium, Temperature, Humidity, pH, Rainfall]])
    predicted=predicted[0]

    print(predicted)
    return render_template("index.html",predicted=f'{predicted}')


if __name__=='__main__':
    app.run()

#80,90,47,26.59743595,79.35898915,6.21084479,107.3944717