pycloudstream
=============

Send a message to spring cloud stream channel.

Example
-------

Command line ``pycloudstream-send`` sends a message to the exchange configured
by Spring Cloud Stream properties defined in the ``application.properties``
file under the given path:

::

  $ pycloudstream-send <properties file path> <message payload>

The module can also be used directly:

  >>> import pycloudstream.rabbit
  >>> configured_send = pycloudstream.rabbit.configure_exchange(path)
  >>> configured_send(message_body)


Installation
------------

Clone and install with pip:

::

  $ pip install -e .
