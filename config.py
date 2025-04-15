import pika
import ssl

RMQ_HOST = 'kebnekaise-01.lmq.cloudamqp.com'
RMQ_PORT = 5671  # tls
RMQ_VIRTUAL_HOST = 'fwhlxvuo'

RMQ_USER = 'fwhlxvuo'
RMQ_PASSWORD = 'BfVFveVU8szNHyJbovNq2PubPdozpQVR'

ssl_context = ssl.create_default_context()

connection_params = pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    virtual_host=RMQ_VIRTUAL_HOST,
    credentials=pika.PlainCredentials(username=RMQ_USER, password=RMQ_PASSWORD),
    ssl_options=pika.SSLOptions(context=ssl_context)
)


def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(parameters=connection_params)
