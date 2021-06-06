from app import app
import urllib.request,json

# Getting api_key
api_key = app.config["NEWS_API_KEY"]
# Getting base url
base_url = app.config["NEWS_API_BASE_URL"]

