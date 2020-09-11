from app import app
import urllib.request, json
from .models.news import Article
from .models import news


News = news.News


api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_BASE_URL']
top_url = app.config['NEWS_TOP_URL']
search_url = app.config['SEARCH_URL']
head_url = app.config['HEADLINE_URL']


def get_news(category):
    news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(news_url) as url:
        news_data = url.read()
        new_news = json.loads(news_data)

        if new_news['sources']:
            source_news = new_news['sources']
            news_sources = process_news(source_news)

    return news_sources


def process_news(news_list):


    news_sources = []
    for newss in news_list:

        name = newss.get('name')
        id = newss.get('id')
        linkurl = newss.get('url')
        des = newss.get('description')
        category=newss.get('category')

        if name:
            sourcesfornews = News(name,id,linkurl,des,category)
            news_sources.append(sourcesfornews)

    return  news_sources


def get_headlines(sources):
    new = top_url.format(sources,api_key)
    with urllib.request.urlopen(new) as url:
        headlineurl= url.read()
        urlforheadlines= json.loads(headlineurl)
        Head= []
        if urlforheadlines['articles']:
            headurl= urlforheadlines['articles']
            Head=process_headline(headurl)

    return Head


def process_headline(new_list):

    topHeadline=[]

    for top in new_list:
        id= top.get('id')
        nameheadline=top.get('title')
        image = top.get('urlToImage')
        link = top.get('url')
        timepublished = top.get('publishedAt')
        description = top.get('description')

        if image:
            head = Article(id,nameheadline,image,link,timepublished,description)
            topHeadline.append(head)
    return topHeadline


def get_search(query):
    search = search_url.format(query,api_key)

    with urllib.request.urlopen(search) as urls:
        searchurl= urls.read()
        urlforsearch= json.loads(searchurl)

        endsearch = []

        if urlforsearch['articles']:
            headurl= urlforsearch['articles']
            endsearch=process_headline(headurl)
        return endsearch




def get_topstories(country):
    top_head = head_url.format(country,api_key)
    with urllib.request.urlopen(top_head) as url:
        headlinedurl= url.read()
        urlfortopstories= json.loads(headlinedurl)
        Head= []
        if urlfortopstories['articles']:
            headurl= urlfortopstories['articles']
            Head=process_headline(headurl)

    return Head














