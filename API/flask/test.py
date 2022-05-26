from flask import Flask, request

app = Flask(import_name="Prueba")

@app.route("/holaMundo", methods=['GET'])
def holaMundo():
    return "Hola Mundo"

@app.route("/hola", methods=['GET'])
def hola():
    nombre = request.args.get('nombre')

    if nombre is None:
        text = 'Hola!'
    else:
        text = 'Hola ' + nombre + '!'
    return text


if __name__ == "__main__":
    app.run(debug=True, port=8000)