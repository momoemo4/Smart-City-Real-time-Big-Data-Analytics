import storm
import json
import re
from cassandra.cluster import Cluster
import blist
from sklearn import svm
from sklearn.externals import joblib
import datetime
#------- Load Clf files -------
svmFog = joblib.load(‘svmFog.pkl’)
svmHaze = joblib.load(‘svmHaze.pkl’)
#----- Connect to Cassandra -----

cluster = Cluster([‘127.0.0.1’])
session = cluster.connect(‘predictions’)

def analyzeData(data):
    fog_predict = svmFog.predict(data)
    haze_predict = svmHaze.predict(data)
    return [str(fog_predict[0]), str(haze_predict[0])]

class SensorBolt(storm.BasicBolt):
    def process(self, tup):
        data = tup.values[0]

        output = analyzeData(data)
        result = "Result: "+ str(output)
        timestamp= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #Store analyzed results in Cassandra
        session.execute(
        """
        INSERT INTO data(timestamp, fog_prediction, haze_prediction)
        VALUES (%s, %s, %s)
        """,
        (timestamp, output[0], output[1])
        )
        
        storm.emit([result])
        
SensorBolt().run()
