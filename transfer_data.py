# transfer_data.py
# server.py
import os
import time
from shutil import copyfile

BASE_DIR = 'server/'
NET_DIR = 'net/'


def main():
    filenames = os.listdir(BASE_DIR)
    for i, filename in enumerate(filenames):
        print('copying {} into net drive... {}/{}'.format(filename, i + 1,
                                                          len(filenames)))
        copyfile(BASE_DIR + filename, NET_DIR + filename)
        print(
            'copied {} into net drive, waiting client complete... {}/{}'.format(
                filename, i + 1, len(filenames)))
        while os.path.exists(NET_DIR + filename):
            time.sleep(3)
        print('transferred {} into client. {}/{}'.format(filename, i + 1,
                                                         len(filenames)))


if __name__ == '__main__':
    main()

# client.py

BASE_DIR = 'client/'
NET_DIR = 'net/'


def main():
    while True:
        filenames = os.listdir(NET_DIR)
        for filename in filenames:
            print('downloading {} into local disk...'.format(filename))
            copyfile(NET_DIR + filename, BASE_DIR + filename)
            os.remove(NET_DIR + filename)
            print('downloaded {} into local disk'.format(filename))
        time.sleep(3)


if __name__ == "__main__":
    main()
