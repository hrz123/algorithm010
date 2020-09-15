# duck-typing.py


class Logger:
    def record(self):
        print("I write a log info file.")


class DB:
    def record(self):
        print("I insert data into db.")


def test(recorder):
    recorder.record()


def main():
    logger = Logger()
    db = DB()
    test(logger)
    test(db)


if __name__ == '__main__':
    main()
