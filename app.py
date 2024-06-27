from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS= [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Carabobo, San Diego',
    'salary':'$100,000'
  },
  {
    'id':2,
    'title':'Data Science',
    'location':'Barcelona, San Diego',
    'salary':'$150,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'Remote',
    'salary':'$120,000'
  },
]
@app.route("/")
def hello():
  return render_template("home.html",jobs=JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

                 
if __name__ == "__main__":
  print("i am inside")
  app.run(host='0.0.0.0', debug=True)
