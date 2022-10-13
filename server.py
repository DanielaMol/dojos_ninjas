from dojos_ninjas_app import app
from dojos_ninjas_app.controllers import dojos, ninjas
app.secret_key = "estessecreto"


if __name__=="__main__":
    app.run(debug=True)