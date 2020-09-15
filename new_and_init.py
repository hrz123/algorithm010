# new_and_init.py


class Student(object):
    def __new__(cls, *args, **kwargs):
        print('class.__new__ called')
        return super(Student, cls).__new__(cls)

    def __init__(self, name, height):
        print('class.__init__ called')
        self.name = name
        self.height = height

    def __str__(self):
        return "The height of Student %s if %s" % (self.name, self.height)


class PositiveInteger(int):
    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))


def main():
    xiaoming = Student('xiaoming', 175)
    print(xiaoming)

    a = PositiveInteger(-10)
    print(a)


if __name__ == '__main__':
    main()
