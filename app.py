from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('myForm.html')

@app.route('/submit',methods=['POST'])
def submit():
    firstname=request.form['firstname']
    lastname=request.form['lastname']
    age=request.form['age']
    return render_template('greetings.html',name1=firstname,name2=lastname,age=age)

if __name__=="__main__":
    app.run(host='0.0.0.0', port= 5000, debug = True)