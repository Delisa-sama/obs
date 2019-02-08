import time
from watchdog.observers import Observer

from fshandler import FSHandler
from loghandler import LogHandler
import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Observe files.')
    parser.add_argument('path', type=str, help='Path to observe.')

    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    observer = Observer()
    observer.schedule(FSHandler(), args.path, recursive=True)
    observer.schedule(LogHandler(), args.path, recursive=True)
    observer.start()

    print("Observer started on path {}".format(args.path))
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
