import requests
import json
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
response = requests.get('https://api.openweathermap.org/data/2.5/weather?id=2158177&units=metric&appid=ec22808df862ff0aa7e0601d85536ca4')
data = response.text
parse_json = json.loads(data)
temp = parse_json['main']['temp']

producer.send('sample', json.dumps(parse_json).encode('utf-8'))

