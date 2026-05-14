

from flask import Flask, request, Response
import requests

app = Flask(__name__)



@app.route("/input", methods=["GET", "POST"])
def check_size():
    size = request.content_length or 0
    one_GB = 1024**3
    if size > one_GB:
        return "The file is too big"
    else:
        resp = requests.get(f"{SITE_NAME}{path}")
        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
        headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response



# curl -X POST "http://192.168.100.4:12345" -F "file=@test.txt"
