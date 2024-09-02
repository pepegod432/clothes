from flask import *
from firebase import firebase

import json
firebase = firebase.FirebaseApplication("https://heigth-quality-clothes-default-rtdb.firebaseio.com/",None)

def cosneguir_productos():
	a = firebase.get("/productos/","")
	c = str(a)
	c = c.replace("'",'"')
	b = json.loads(c)
	products = list(b.values())
	return products
app = Flask(__name__)



@app.route("/")
def index():
  data = cosneguir_productos()
  print(data)
  return render_template("main.html",data=data)
@app.route("/shirt")
def xd():
  return render_template("productos.html",data=(1,2,3,4,5))

if __name__ == "__main__":
   app.run(port=3000,debug=True)
