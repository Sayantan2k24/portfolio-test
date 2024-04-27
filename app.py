from flask import Flask, render_template # from flask module import Flask Class

# next create an object from flask and puting it in the variable
# if the program is invoked by python app.py --> then print(__name__) ==> will be output as main

app = Flask(__name__)

# then need to create a route
# register a route
# @ --> decorator
@app.route("/") # now define a function  below the decorator
def hello_profile():
    return render_template('home.html')

if __name__ == '__main__': #we are checking if we are running this python script as python app.py --> then do start this app by app.run --> and these are the arg --> and debug is True --> update on the fly
    app.run('0.0.0.0', debug=True)

