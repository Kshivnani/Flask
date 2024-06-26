from flask import Flask
app=Flask(__name__)

@app.route('/')
def Welcome():
    return 'Hello My Name is Kapil Shivnani'

@app.route('/Member')
def Member():
    return 'Hello Members'


if __name__ == '__main__':
    app.run(debug=True)

