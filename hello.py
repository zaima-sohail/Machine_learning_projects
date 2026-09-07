from flask import Flask,request, render_template
app=Flask(__name__)
@app.route("/")
def input_user():
   return render_template("input.html")
@app.route("/sumbit",methods=["POST"])
def send():
    name=request.form["username"]
    email=request.form["email"]
    password=request.form["password"]
    return f"Hello,{name}! ,{email},{password}"
            



if __name__=="__main__":
  app.run(debug=True,use_reloader=False)