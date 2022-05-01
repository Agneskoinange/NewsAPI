import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'http://newsapi.org/v2/sources?&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # NEWS_API_BASE_URL = 'http://newsapi.org/v2/sources?&apiKey=1e51b99e9ee04378b5c113f9b700eb45'
    # 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=1e51b99e9ee04378b5c113f9b700eb45'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True