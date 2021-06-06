from app import app
import urllib.request,json
from .models import news


News = news.News
Sources = news.Sources
# Getting api_key
api_key = app.config["NEWS_API_KEY"]
# Getting base url
base_url = app.config["NEWS_API_BASE_URL"]

# __________________________News class ________________________

def get_news(category):
    """
    Function that gets the json response to our url reques
    """
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        # confirming whether the response has any data
        if get_news_response["articles"]:
            news_results_list = get_news_response["articles"]
            news_results = process_results(news_results_list)
    
    return news_results
# if data is found,process it here

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    # To store our newly created news objects
    news_results = []

    # Accessing only the required values using a for loop
    for news_item in news_list:
        title = news_item.get("title")
        description = news_item.get("description")
        url = news_item.get("url")
        urlToImage = news_item.get("urlToImage")
        publishedAt = news_item.get("publishedAt")

        # incase the artcles might not have an image we create a condition to cover that image
        if urlToImage:
            news_object = News(title,description,url,urlToImage,publishedAt)
            news_results.append(news_object)

    return news_results



# ___________________________Source class__________________________________________________________________

def sources_news():
    '''
    Function that gets the json response to our url request
    '''
    # Getting base url
    sources_url = "https://newsapi.org/v2/sources?apiKey={}".format(api_key)
    get_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        search_sources_data = url.read()
        search_sources_response = json.loads(search_sources_data)

        search_sources_results = None

        if search_sources_response["sources"]:
            search_sources_list = search_sources_response["sources"]
            search_sources_results = process_sources(search_sources_list)

    return search_sources_results

# Processing the sources

def process_sources(sources_list):
    """
    Function  that processes the sources result and transform them to a list of Objects
    """

    sources_results = []

    for sources_item in sources_list:
        id = sources_item.get("id")
        name = sources_item.get("name")
        description = sources_item.get("description")
        url = sources_item.get("url")
        category = sources_item.get("category")

        # for the sources that might have trouble with urls
        if url:
            sources_object = Sources(id, name, description, url, category)
            sources_results.append(sources_object)

    return sources_results


# _______________________________search For News__________________________________________________________

    