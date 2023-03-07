from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():

    name = "Teja"
    age = "14" 

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def home1():

    name = "Dad"
    age = "45" 

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def home2():

    name = "Mom"
    age = "39" 

    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def home3():

    name = "Friend"
    age = "14" 

    return render_template('friend.html' , name = name , age = age)


if __name__  ==  '__main__':
    app.run(debug=True)
