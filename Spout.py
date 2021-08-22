from storm import Spout, emit, log
from kafka.client import KafkaClient
from kafka.consumer import KafkaConsumer
from kafka.producer import SimpleProducer
from kafka.consumer import SimpleConsumer

client = KafkaClient("localhost:9092")
consumer = KafkaConsumer("sample",
    metadata_broker_list=["localhost:9092"])

def getData():
    data = consumer.next().value
    return data

class SensorSpout(Spout):
    def nextTuple(self):
        data = getData()
        emit([data])
SensorSpout().run()

