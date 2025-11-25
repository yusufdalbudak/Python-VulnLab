import requests
from flask import Flask, request, abort
from urllib.parse import urlparse

app = Flask(__name__)

ALLOWED_DOMAINS = ["example.com", "api.trusted.com"]

@app.route('/download')
def download():
    url = request.args.get('url')
    if not url:
        abort(400)
    
    # FIX: Validate the URL scheme and domain
    parsed = urlparse(url)
    if parsed.scheme not in ["http", "https"]:
        abort(400, "Invalid scheme")
        
    if parsed.netloc not in ALLOWED_DOMAINS:
        abort(403, "Domain not allowed") # FIX: Prevent SSRF
        
    try:
        response = requests.get(url, timeout=5) # FIX: Add timeout
        return response.content
    except requests.RequestException:
        abort(500)
