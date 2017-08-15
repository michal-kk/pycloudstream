"""Send message to RabbitMQ."""
from functools import partial
import pika


def send_message(message_body, rabbit_address, rabbit_port, to_exchange):
    """Send message to the specified RabbitMQ exchange.

    Args:
        message_body (str): The body (payload) of the message.
        rabbit_address (str): IP address of the RabbitMQ broker.
        rabbit_port (int): Port of the RabbitMQ broker.
        to_exchange (str): Name of the exchange.
    """
    try:
        connection_parameters = pika.ConnectionParameters(rabbit_address,
                                                          rabbit_port)
        connection = pika.BlockingConnection(connection_parameters)
        channel = connection.channel()

        channel.basic_publish(exchange=to_exchange,
                              routing_key="key",
                              body=message_body,
                              properties=pika.BasicProperties(
                                  content_type="application/json"))
    finally:
        connection.close()


simple_send = partial(send_message,
                      rabbit_address="192.168.99.100",
                      rabbit_port=5672,
                      to_exchange="my-message-queue")
"""partial: Convinience function to send message to a predefined exchange."""
