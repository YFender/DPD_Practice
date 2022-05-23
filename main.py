import flask
import kafka

app = flask.Flask(__name__)
producer = kafka.KafkaProducer(bootstrap_servers='localhost:9092')


@app.post("/foobar")
def foobar():
    if flask.request.is_json:
        future = producer.send("foobar_topic", flask.request.json)
        if future.failed():
            for i in range(100):
                future = producer.send("foobar_topic", flask.request.json)
                if not future.failed():
                    break
                else:
                    if i == 99:
                        return 500
            return 200
        else:
            return 200

if __name__ == "__main__":
    app.run(port=5050)