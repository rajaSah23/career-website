from flask import Flask
app= Flask( __name__ ) # create app object

@app.route("/")  # create root route (Same as Express.js)
def hello_world():
    return "Hello from server side"


# Note: we can't directly run a Flask file like noraml python file.ie: pyhton app.py, so we need this:
if __name__ == "__main__":     #if the file is flask file
    app.run(host='0.0.0.0',debug=True)  # run on localhost