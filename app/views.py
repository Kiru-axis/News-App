from flask import render_template
from app import app
from .request import get_news

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

