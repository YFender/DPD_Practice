from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(1):
    future = producer.send('TutorialTopic', b'some_message_bytes')
    print(future.failed())
