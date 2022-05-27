from flask import Flask, request, jsonify, send_file

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

@app.route("/holaJson", methods=['GET'])
def holaJson():
    nombre = request.args.get('nombre')

    if nombre is None:
        text = 'Hola!'
    else:
        text = 'Hola ' + nombre + '!'
    return jsonify({"mensaje": text})

@app.route("/get-iris")
def get_iris():

    import pandas as pd
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    return jsonify({
        "message": "Iris Dataset",
        "data": iris.to_dict()
        })

@app.route("/plot-iris")
def plot_iris():

    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('img/iris.png')

    return send_file('img/iris.png')

if __name__ == "__main__":
    app.run(debug=True, port=8000)