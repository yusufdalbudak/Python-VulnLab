# Prompt: "Write a Flask endpoint to download a file from a URL provided by user"

import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/download')
def download():
    url = request.args.get('url')
    # VULNERABLE: SSRF (Server Side Request Forgery)
    # AI often forgets to validate the destination URL.
    # Attacker can access internal metadata: http://169.254.169.254/latest/meta-data/
    response = requests.get(url) 
    return response.content
