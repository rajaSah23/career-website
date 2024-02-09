from flask import Flask, render_template, jsonify
app= Flask( __name__ ) # create app object

@app.route("/")  # create root route (Same as Express.js)
def hello_world():
    # return "Hello from server side"
    return render_template('home.html')

jobs=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi, India',
    'salary':'Rs. 15,00,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':'Rs. 12,00,000'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco, USA',
    'salary':'$120,000'
  }
]

@app.route("/jobs")  #render html/template with dynamic data
def list_jobs():
  
  return render_template('jobs.html',jobs=jobs)


# Sending response as JSON file
@app.route("/api/jobs") 
def api_route():
  return jsonify(jobs)



# Note: we can't directly run a Flask file like noraml python file.ie: pyhton app.py, so we need this:
if __name__ == "__main__":     #if the file is flask file
    app.run(host='0.0.0.0',debug=True)  # run on localhost