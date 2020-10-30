from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('RFC95.pkl')

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/pred.html")
def predict():
    return render_template('pred.html')
    
@app.route("/result", methods=["POST"])
def result():
    creatinine_phosphokinase = request.form['creatinine_phosphokinase']
    ejection_fraction = request.form['ejection_fraction']
    platelets = request.form['platelets']
    serum_creatinine = request.form['serum_creatinine']
    time_in_clinic = request.form['time_in_clinic']
    result = int(model.predict([[creatinine_phosphokinase, ejection_fraction, platelets, serum_creatinine, time_in_clinic]])[0])
    
    if result == 0:
        return render_template("negative.html")
    else:
        return render_template("positive.html")




if __name__ == "__main__":
    app.run()