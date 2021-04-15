from flask import Flask, render_template
from secrets import api_key
import requests
app = Flask(__name__)

@app.route('/')
def welcome():
    return '<h1>Welcome!</h1>'
    
@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm)  
   
@app.route('/headlines/<nm>')
def headline(nm):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    para_dic = {'api-key': api_key}
    response = requests.get(base_url, para_dic)
    res = response.json()['results'][:5]
    headlines = [r['title'] for r in res]
    return render_template('headline.html', name=nm, stories=headlines)

@app.route('/links/<nm>')
def link(nm):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    para_dic = {'api-key': api_key}
    response = requests.get(base_url, para_dic)
    res = response.json()['results'][:5]
    # headlines = [r['title'] for r in res]
    # urls = [r['url'] for r in res]
    infos = [[r['title'], r['url']] for r in res]
    return render_template('link.html', name=nm, infos=infos)

@app.route('/images/<nm>')
def image(nm):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    para_dic = {'api-key': api_key}
    response = requests.get(base_url, para_dic)
    res = response.json()['results'][:5]
    headlines = [r['title'] for r in res]
    urls = [r['url'] for r in res]
    thumbnails = []
    for r in res:
        multimedia = r['multimedia']
        for m in multimedia:
            if m['format'] == 'Standard Thumbnail':
                thumbnails.append(m['url'])
    infos = []
    for i in range(len(headlines)):
        info = [headlines[i], urls[i], thumbnails[i]]
        infos.append(info)
    return render_template('image.html', name=nm, infos=infos) 

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)
