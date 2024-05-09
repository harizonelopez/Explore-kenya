from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'alladinh00-010montext'



if __name__ == "__main__":
    app.run(debug=True)