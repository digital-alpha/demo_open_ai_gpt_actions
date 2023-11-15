import json
from flask import Flask, request, send_file, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://chat.openai.com"}})

@app.route("/todos", methods=["GET"])
def getTodos():
    return Response(response=json.dumps({"item": "pick jacket"}), status=200)

@app.route("/logo.png", methods=["GET"])
def plugin_logo():
    filename = 'logo.png'
    return send_file(filename, mimetype='image/png')

@app.route("/.well-known/ai-plugin.json", methods=["GET"])
def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return Response(text, mimetype="text/json")

@app.route("/openapi.yaml", methods=["GET"])
def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=443, ssl_context='adhoc')

if __name__ == "__main__":
    main()
