import pycloudstream.rabbit
import sys


def main():
    simple_send = pycloudstream.rabbit.configure_exchange(sys.argv[1])
    simple_send(sys.argv[2])
