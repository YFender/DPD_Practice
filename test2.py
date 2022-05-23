from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(1):
    print('some_message_bytes'.encode())
    future = producer.send('TutorialTopic', 'some_message_bytes'.encode())
    print(future.get())
    future = producer.send('foobar', 'some_message_bytes'.encode())
    print(future.get())