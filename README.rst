pycloudstream
=============

Send a message to spring cloud stream channel.

Example
-------

Executing ``pycloudstream-send`` with an argument sends a message to the
predefined RabbitMQ exchange:

::

  $ pycloudstream-send {"example-key":"example-value"}


Installation
------------

Clone and install with pip:

::

  $ pip install -e .
