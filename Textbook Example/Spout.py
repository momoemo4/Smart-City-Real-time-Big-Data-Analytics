from storm import Spout, emit, log
from kafka.client import KafkaClient
from kafka.consumer import KafkaConsumer
from kafka.producer import SimpleProducer
from kafka.consumer import SimpleConsumer

client = KafkaClient("127.0.0.1:6667")
consumer = KafkaConsumer("weather",
    metadata_broker_list=[‘127.0.0.1:6667’])

def getData():
    data = consumer.next().value
    data = data.replace(‘[’,”).replace(’]’,”).split(‘,’)
    data = [ float(x) for x in data ]
    return data

class SensorSpout(Spout):
    def nextTuple(self):
        data = getData()
        emit([data])
        
SensorSpout().run()
