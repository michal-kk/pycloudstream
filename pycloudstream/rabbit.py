"""Send a message to RabbitMQ.

This module reads java properties file, configures a RabbitMQ exchange based on
spring cloud stream properties in the file and sends a message to the
configured exchange.

Example:
    ...

Todo:
    * Handle channels other than ``input``.
"""
import functools
import pika
import javaproperties
import os


def configure_exchange(properties_file_path):
    """Read properties file, return send message function.

    Args:
        properties_file (str): Path of the ``application.properties`` file
            containing spring cloud stream configuration.

    Returns:
        Partial that takes a message body as an argument and sends the given
            message body to the exchange configured via the read parameters.
    """
    with open(os.path.join(properties_file_path, "application.properties"),
              "rb") as f:
        properties_dict = javaproperties.load(f)

    properties_address, properties_port = properties_dict[
        "spring.rabbitmq.addresses"].split(",")[0].split(":")
    properties_exchange = properties_dict[
        "spring.cloud.stream.bindings.input.destination"]

    return functools.partial(send_message,
                             rabbit_address=properties_address,
                             rabbit_port=int(properties_port),
                             to_exchange=properties_exchange)


def send_message(message_body, rabbit_address, rabbit_port, to_exchange):
    """Send a message to the specified RabbitMQ exchange.

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
