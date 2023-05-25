from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'Title': 'Data Analyst',
    'Location': 'Bengaluru',
    'Salary': 'Rs. 10,00,000'
  },
    {
    'id': 2,
    'Title': 'Data Engineer',
    'Location': 'Bengaluru',
    'Salary': 'Rs. 10,00,000'
  },
    {
    'id': 3,
    'Title': 'Data Infrastructure Manager',
    'Location': 'Bengaluru'
  },
    {
    'id': 4,
    'Title': 'Senior Data Analyst',
    'Location': 'Bengaluru',
    'Salary': 'Rs. 10,00,000'
  }
]

@app.route('/')
def hello_world():
    return render_template('test.html',jobs=JOBS)

@app.route('/jobs')
def json():
  return jsonify(JOBS)

if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)
  