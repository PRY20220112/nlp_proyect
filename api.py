from flask import Flask, request
import servicioNlp

app = Flask(__name__)


@app.route('/test/', methods=['GET'])
def test_deploy():
    return 'Hello World'


@app.route('/spacy/', methods=['POST'])
def request_file():
    try:
        texto = request.json['texto']
    except Exception as e:
        print(e)
        return '{"response": "Bad Request", "message": "The request needs a texto parameter"}', 400

    if len(texto) == 0:
        return '{"response": "Bad Request", "message": "the length of the text cannot be zero"}', 400
    try:
        respuesta = servicioNlp.procesar_texto(texto)
    except Exception as e:
        print(e)
        return '{"response": "Server Error"}', 500
    json = respuesta.json
    return json, 200


if __name__ == '__main__':
    app.run(debug=True, port=4000)
