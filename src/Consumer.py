from confluent_kafka import Consumer, KafkaError, KafkaException
import sys
import io

conf = {
    "bootstrap.servers": "broker:9092",
    "group.id": "foo",
    "auto.offset.reset": "smallest",
}
running = True
cons = Consumer(conf)


def consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        msg_count = 0
        while running:
            msg = consumer.poll(timeout=3.0)
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write(
                        "%% %s [%d] reached end at offset %d\n"
                        % (msg.topic(), msg.partition(), msg.offset())
                    )
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                # data = io.StringIO(msg.value().decode("utf-8"))
                # print(data.readline())
                data = msg.value().decode("utf-8")
                print(data)
                msg_count += 1
                if msg_count > 1:
                    consumer.commit(asynchronous=False)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()


consume_loop(cons, ["test"])
