from flask import Flask, render_template, request, url_for
from models import ParseResult, JsonResult
from dataAccess import Dao
import json
from ranking import Ranking

app = Flask(__name__)

page_title = "le.utah.gov Search"

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title=page_title)

@app.route('/about')
def about():
    return render_template('about.html', title='About Page')

@app.route('/search', methods = ['POST', 'GET'])
def search():
    query_str = request.args.get('q')
    if (request.method == 'POST'):
        query_str = request.form['q']
    
    print(f'query_str[{query_str}]')

    ranking = Ranking()
    dao = Dao()
    pr_list = dao.getContent(query_str)
    for link in pr_list:
        ranking.rank(link, query_str)
    pr_list.sort(key=lambda x: x.score, reverse=True)

    print('search results', len(pr_list))

    dao.close()

    r_count = '{:,}'.format(len(pr_list)) 

    return render_template('home.html', title=page_title, data=pr_list, searchTerm=query_str, resultCount=r_count)

if __name__ == '__main__':
    app.debug = True
    app.run()