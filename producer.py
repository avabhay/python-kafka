from kafka import KafkaProducer
import time
import os

KAFKA_SERVER = 'localhost:9092'
KAFKA_TOPIC =  'demo-topic'
EMAIL_FILE = 'emails.txt'

def send_email_to_kafka(email):
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    seen_emails = set()
    while True:
        if os.path.exists(EMAIL_FILE):
            with open(EMAIL_FILE, 'r') as file:
                for email in file:
                    email = email.strip()
                    if email not in seen_emails:
                        seen_emails.add(email)
                        producer.send(KAFKA_TOPIC, value=email.encode('utf-8'))
                        print(f"Email {email} sent to Kafka topic {KAFKA_TOPIC}")
        time.sleep(2)
    producer.flush()
    producer.close()
if __name__ == "__main__":
    send_email_to_kafka(EMAIL_FILE)
# This code reads emails from a file and sends them to a Kafka topic.
# It uses a set to keep track of seen emails to avoid duplicates.
# The producer sends emails to the Kafka topic every 5 seconds.
# The producer is closed after sending all emails.
# The code is designed to run indefinitely, continuously checking for new emails in the file.
# The Kafka server is assumed to be running on localhost:9092.
# The topic name is 'demo-topic'.
