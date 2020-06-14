from flask import Flask
from flask import render_template
from flask import request,jsonify
from pyfuncs.helper import Helper
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def details():
    return render_template('index.html')

@app.route('/parse_data',methods=['GET','POST'])
def parse_data():
    if request.method == "POST":
        response =request.get_json()
        addHelper = Helper(int(response['release']),int(response['product']))
        addValue = addHelper.add()
        subValue = addHelper.sub()
        mulValue = addHelper.mul()
        divValue = addHelper.div()
        print (addValue)
    data = {'Add Value':addValue,'Sub Value':subValue,'Mul Value':mulValue,'Div Value':divValue}
    return jsonify({'results':render_template('_calc_template.html',data=data)})

if __name__ == '__main__':
    app.run(debug=True)