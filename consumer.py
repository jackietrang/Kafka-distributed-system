
import json

from kafka import KafkaProducer, KafkaConsumer

def is_celebrity(profile):
    return profile['followers_num'] >= 100000

PRODUCER_TOPIC = "my-topic-three"
FAMOUS_TOPIC = "test_famous_topic"
NORMAL_TOPIC = "test_normal_topic"

if __name__ == '__main__':
    consumer = KafkaConsumer(
        PRODUCER_TOPIC,
        bootstrap_servers=['localhost:9091', 'localhost:9092', 'localhost:9093'],
        api_version=(0,11,5),
        value_deserializer=lambda value: json.loads(value),
    )
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9091', 'localhost:9092', 'localhost:9093'],
        api_version=(0,11,5),
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    for message in consumer:
        profile = dict(message.value)
        topic = FAMOUS_TOPIC if is_celebrity(profile) else NORMAL_TOPIC
        producer.send(topic, value=profile)
        print("This is from consumer, with topic", topic, profile)
