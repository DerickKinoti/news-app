from app import app
from flask import render_template,url_for,request,redirect

from .requests import get_news,get_headlines,get_search,get_topstories
@app.route('/')
def headline():

    sports =get_news('sports')
    business=get_news('business')
    technology=get_news('technology')
    entertainment = get_news('entertainment')


    toplines=get_topstories('us')
    search_url= request.args.get('search_article')
    if search_url:
        return redirect(url_for('search',query=search_url))
    else:
        return render_template('index.html', sports=sports,headlines=toplines,business=business,technology=technology,entertainment=entertainment)

@app.route('/sources/<sources>')
def index(sources):
    topheadline = get_headlines(sources)
    title = 'Welcome to the news website'
    if topheadline:
        return render_template('news.html', title = title,heads=topheadline)
    else:

        return render_template('blanksource.html')




@app.route('/search/<query>')
def search(query):
    search_list=query.split(" ")
    new_search="+".join(search_list)
    newst=get_search(new_search)
    if newst:
        return render_template('search.html',search=newst)
    else:
        return render_template('blank.html')

@app.errorhandler(404)
def err(error):
    return render_template('error.html'), 404

