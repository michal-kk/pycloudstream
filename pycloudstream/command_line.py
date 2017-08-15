import pycloudstream.rabbit
import sys


def main():
    pycloudstream.rabbit.simple_send(sys.argv[1])
