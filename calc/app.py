# Put your app in here.
from flask import Flask,request
from operations import add,sub,mult,div

app = Flask(__name__)

@app.route("/<operation>")
def addfunction(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])

    if operation == "add":
        result = add(a,b)
        return str(result)
    elif operation == "sub":
        result = sub(a,b)
        return str(result)
    elif operation == "mult":
        result = mult(a,b)
        return str(result)
    elif operation == "div":
        result = div(a,b)
        return str(result)


operation = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<op>")
def do_math(op):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    math = operation.get(op)(a,b)
    return str(math)
