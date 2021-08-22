from flask import Flask
import urllib2
app = Flask(__name__)
import blist

from cassandra.cluster import Cluster

cluster = Cluster([‘127.0.0.1’])
session = cluster.connect(‘predictions’)

@app.route(‘/’)
def tweet_home():

    html = ‘<html><body><table width=80% border=1 align="center">’+
        ‘<tr><td><strong>Timestamp</strong></td>’+
        ‘<td><strong>Fog Prediction</strong></td>’+
        ‘<td><strong>Haze Prediction</strong></td></tr>’

    data = session.execute(‘SELECT * FROM data’)
    for each in data:
        html+=‘<td>’+each.timestamp+‘</td><td>’+
        each.fog_prediction+‘</td><td>’+
        each.haze_prediction+‘</td></tr>’
    html+=‘</table></body></html>’

    return html

if __name__ == ‘__main__’:
app.run(host=‘0.0.0.0’)
