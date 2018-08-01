from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Method used: %s" % request.method

@app.route ("/bacon", methods=["GET", "POST"])  #different request methods to handle different ways
def bacon():                                       # shows that this is getting post and get
    
    if request.method == "POST":
        return "You are using post"
    else:
        return "Your using post"
        

if __name__ == "__main__":
    app.run()