from flask import Flask
app=Flask(__name__)
@app.route('/')
def Website():
   return "<html><body><h1>This is heading 1</h1></body></html>"

if __name__ =='__main__':
   app.run(debug=True)

