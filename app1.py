from flask import Flask
# creating the flask class object
app=Flask(__name__)
# decorator defines the
@app.route('/')
def home():
    return "hello,this is our first flask website";

if __name__=='__main__':
   app.run(debug=True)
