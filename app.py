from flask import Flask, request, render_template
import pickle


app = Flask(__name__)

pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def result():
    if request.method == 'POST':
        Variance = request.form['Variance']
        Skewness = request.form['Skewness']
        Curtosis = request.form['Curtosis']
        Entropy = request.form['Entropy']

        prediction = classifier.predict([[Variance,Skewness,Curtosis,Entropy]])
        return render_template('result.html',result = prediction)



if __name__ == '__main__':
    app.run(debug=True)