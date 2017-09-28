from flask import Flask,request
import urllib2
import math,random,json
from bs4 import BeautifulSoup

app = Flask(__name__)

URL = 'https://api.douban.com/v2/movie/top250'


def req_url(url):
    response = urllib2.urlopen(url)
    data = response.read()
    return data

@app.route('/')
def index():
    index = int(random.random() * 19)

    start = request.args.get('start','0')
    count = request.args.get('count','1')
    print start,count

    movieURL = URL+'?start='+start+'&count='+count

    jsondata = json.loads(req_url(movieURL))

    URLComments = jsondata['subjects'][0]['alt'] + 'comments'

    soup = BeautifulSoup(req_url(URLComments), "html.parser")

    comments = soup.find_all(class_="comment")

    oneComment = comments[index].p.string

    jsondata['subjects'][0]['comment'] = oneComment

    print jsondata



    return json.dumps(jsondata)


if __name__ == '__main__':
    app.run()
