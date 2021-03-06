import os
# os module that will allow our application to interact with the operating system dependent functionality
class Config:
    '''
    General confirguration parent class
    '''
    # We use the os.environ.get() function to get MOVIE_API_KEY and SECRET_KEY which we will set as environment variables.
    NEWS_API_BASE_URL = "https://newsapi.org/v2/{}?country=us&apiKey={}"
    SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')    


class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General confirguration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General confirguration settings
    '''

    DEBUG = True
# We then create a dictionary config_options to help us access different configuration option classes

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}