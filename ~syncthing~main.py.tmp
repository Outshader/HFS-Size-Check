

from flask import Flask, request
import requests
from jinja2 import defaults

app = Flask(__name__)



def check_size(path=''):
    size = request.content_length or 0
    one_GB = 1024**3
    if size > one_GB:
        return "The file is too big"
    else:
        # forward to HFS




# curl -X POST "http://192.168.100.4:12345" -F "file=@test.txt"
