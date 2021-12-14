import json
from time import sleep

from kafka import KafkaProducer
from random_messages import create_random_influencer_profiles

PRODUCER_TOPIC = "my-topic-three"


if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9091', 'localhost:9092', 'localhost:9093'],
        api_version=(0,11,5),
        # Encode all values as JSON
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    while True:
        profile: dict = create_random_influencer_profiles()
        producer.send(PRODUCER_TOPIC, value=profile)
        print("This is profile from producer", profile)  
  
