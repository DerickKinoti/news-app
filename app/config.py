class Config:
    NEWS_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_TOP_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    SEARCH_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    HEADLINE_URL = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'

class ProdConfig:
    pass

class DevConfig:
    DEBUG = True
