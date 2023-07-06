from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  return render_template('index.html')


@app.route("/create")
def form_creation():
  return render_template('form_creation.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
