from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit',methods=['POST'])
def submit():
    un=request.form['username']
    return render_template('greeting.html',un=un)

if __name__=="__main__":
    app.run(host='0.0.0.0', port= 5000, debug = True)
