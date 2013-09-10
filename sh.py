import os 
import re
import requests
from requests_oauthlib import OAuth1
from flask import render_template
from flask import Flask
import sys

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
# ...
app = Flask('myapp', template_folder=tmpl_dir)
app = Flask(__name__)

BASE_URL = u'https://api.twitter.com/1.1/'

client_key = u'OWEFrGWjcUPyTFHhHnT2Q'
client_secret = u'b120PIQFjz8l2TNijVxf3vkyK1o7f7sFaBqhyeTFc'
resource_owner_key = u'1746056306-2QatczLqgaO5XMGyBuxqPaPVHN8JW5R6kJcEx9g'
resource_owner_secret = u'SsWUGJOcJtSaS9zRQz9I8bkgMvF21DpxUcTmgbM'

oauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret)

headeroauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret,
                     signature_type='auth_header')


queryoauth = OAuth1(client_key, client_secret,
                    resource_owner_key, resource_owner_secret,
                    signature_type='query')


bodyoauth = OAuth1(client_key, client_secret,
                   resource_owner_key, resource_owner_secret,
                   signature_type='body')


@app.route('/')			   
def sh():
	payload = {'screen_name': 'syawalhafriz','count':10}
	url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
	r = requests.get(url, auth=oauth,params=payload)
	a=r.json()
	b=[]
	for i in range(payload['count']):
		b.append(a[i]['text'])
	return render_template('sh.html',name=b)

	



