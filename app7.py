from flask import*
app=Flask(__name__)
@app.route('/login',methods=['post'])
def login():
   uname=request.form['uname']
   passwrd=request.form['pass']
   if uname=="punyamurthybhushan@gmail.com" and passwrd=="Bhushaaan":
      return "Welcome %s" %uname
if __name__ =='__main__':
   app.run(debug=True)
