from flask import Flask
app=Flask(__name__)
@app.route('/home')
def Hello():
   return "Hello World";

if __name__=="__main__":
   app.run(debug=True)
