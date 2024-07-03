# Building url dynamically
# Variable rules and url Building

from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my channel"


@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The Result is passed</h1></body></html>" + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The student has failed and the  marks is" + str(score)


##Results checker

@app.route('/results/<int:marks>')
def results(marks):
    results = ""
    if marks<50:
        results = "fail"
    else:
        results = "success"
    return redirect(url_for(results,score=marks))




if __name__ == "__main__":
    app.run(debug=True)
