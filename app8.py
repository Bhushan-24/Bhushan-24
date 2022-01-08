from flask import Flask
app=Flask(__name__)
@app.route('/')
def message():
   return "<html><body><h1>Hi welcome to the website</h1></body></html>"

if __name__ =='__main__':
   app.run(debug=True)
