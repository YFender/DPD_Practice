from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(100):
    future = producer.send('TutorialTopic', b'some_message_bytes')
    print(future.get(timeout=20))
