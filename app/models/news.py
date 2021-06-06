# Articles
class News:
    """
    News class to define News Objects
    """
    def __init__(self, title,description,url,urlToImage,publishedAt):
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

# Sources
class Sources:
    '''
    Sources class to define Sources objects
    '''
    def __init__(self, id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
