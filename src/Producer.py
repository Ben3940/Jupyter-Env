from confluent_kafka import Producer


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


conf = {"bootstrap.servers": "broker:9092", "client.id": "python-producer"}
print(len(df))
producer = Producer(conf)
# for i in range(3):
#     producer.produce("test", key=str(i), value=f"Message {i}", callback=acked)
for idx, row in df.iterrows():
    if idx > 23004:
        break
    producer.produce("test", key=str(idx), value=f"{row}", callback=acked)


producer.poll(2)
