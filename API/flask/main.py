from flask import Flask, jsonify, request, send_file

app = Flask(import_name='Hola Mundo')


@app.route('/hello-world', methods = ['GET'])
def helloworld():
    return "Hello world!"


@app.route('/hello', methods = ['GET'])
def hello():

    name = request.args.get('name')

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello ' + name + '!'

    return text


@app.route('/test-json', methods = ['GET'])
def testJson():

    name = request.args.get('name')

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello ' + name + '!'

    return jsonify({"message": text})


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

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)