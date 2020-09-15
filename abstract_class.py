# abstract_class.py


from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document(Entity):
    def __init__(self):
        self.title = None

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


# 以下为自我练习
class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document(Entity):
    def __init__(self):
        self.title = None

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


def main():
    document = Document()
    document.set_title('Harry Potter')
    print(document.get_title())

    entity = Entity()


if __name__ == '__main__':
    main()
