from flask import Flask 
import flask
import pickle
import numpy as np
import pandas as pd
app=Flask(__name__)
@app.route('/hello')
def HelloWorld():
    return 'Hello World!'



if __name__ =='__main__':  
    app.run(debug = True)
