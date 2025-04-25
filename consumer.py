from kafka import KafkaConsumer

KAFKA_SERVER = 'localhost:9092'
KAFKA_TOPIC =  'demo-topic'

def consumer_from_kafka():
    consumer = KafkaConsumer(KAFKA_TOPIC,
                             bootstrap_servers=KAFKA_SERVER,
                             auto_offset_reset='earliest',
                             enable_auto_commit=True)
    print(f"Waiting for messages...")
    for message in consumer:
        email = message.value.decode('utf-8')
        print(f"New signup Email: {email}")

if __name__ == "__main__":
    consumer_from_kafka()
# # This code consumes messages from a Kafka topic.
# # It uses the KafkaConsumer class to connect to the Kafka server and subscribe to the specified topic.
# # The consumer is set to read messages from the earliest offset and automatically commit offsets.
# # The code prints a message indicating that it is waiting for messages.
# # When a new message is received, it decodes the message value and prints the email.