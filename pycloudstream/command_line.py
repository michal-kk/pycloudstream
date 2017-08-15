import pycloudstream.rabbit
import sys


def main():
    try:
        simple_send = pycloudstream.rabbit.configure_exchange(sys.argv[1])
    except FileNotFoundError:
        try:
            simple_send = pycloudstream.rabbit.configure_exchange(sys.argv[1],
                                                                  True)
        except FileNotFoundError:
            print("The path {} does not contain properties file or spring "
                  "boot project with properties file.".format(sys.argv[1]),
                  file=sys.stderr)
            sys.exit(1)

    simple_send(sys.argv[2])
