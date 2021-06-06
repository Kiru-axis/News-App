from flask import render_template
from app import app
from .request import get_news,sources_news,search_news

@app.route('/')
# view function
def index():
    '''
    View root page function that returns the index page and its data
    '''
    top_headlines = get_news("top-headlines")
    title = "News from News Api"
    return render_template('index.html',title = title,top = top_headlines)


# Sources function and routes
@app.route('/sources')
def sources():
    """
    View function to display sources of the news feed
    """
    source = sources_news()
    title = f"{sources} news"
    message = "Tests"
    return render_template("sources.html", source = source,message = message)

# Search for news feed
@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f" Search results for {news_name}"
    
    return render_template("search.html", news = searched_news)