from flask import Flask

app = Flask(__name__)

def hello():
    return "Hello World!"

@app.route("/")
def hello():
    return "<h1>Paws Rescue Center 🐾</h1>"

@app.route("/about")
def about():
    return """We are a non-profit organization working as an animal rescue. We aim to help you connect with the 
    purrfect furbaby for you! The animals you find on our website are 
    rescued and rehabilitated animals. Our mission is to promote the ideology \"adopt, don't hop\"!"""

@app.route("/<my_name>")
def greetings(my_name):
    if my_name == "kevin":
        my_name = "Dummy"
    return f"welcome {my_name}"

@app.route('/square/<int:number>')
def show_square(number):

    return "Square of "+ str(number) +" is: "+ str(number * number) 

@app.route("/educative")
def learn():
    return "Happy Learning!"

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)



