from random import randrange
import time
import datetime
from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer
import csv
import json
import time

#Connect to Kafka
#change to private DNS
client = KafkaClient("127.0.0.1:6667")
producer = SimpleProducer(client)

def is_number(s):
    try:
        float(s) except ValueError:
        return False
    return True

def sysTest(filename):
    f = open(filename)
    csv_f = csv.reader(f)
    tList=[]
    tClass=[]
    counter=0
    for row in csv_f:
        new_list=[]
        if counter < 2:
            counter=counter+1
            continue
        for item in row:
            if not(is_number(item)):
                continue
            new_list.append(float(item))
        #print new_list
        if len(new_list)!=5:
            continue
        dataSend=json.dumps(new_list).encode(‘utf-8’)
        producer.send_messages(‘weather’,dataSend)
        time.sleep(5)
        print dataSend
        print type(dataSend)
    f.close()


if __name__ == ‘__main__’:
    print ‘Publishing...’
    sysTest(‘PositiveFog.csv’)
    sysTest(‘PositiveHaze.csv’)
    sysTest(‘NegativeFogHaze.csv’)
