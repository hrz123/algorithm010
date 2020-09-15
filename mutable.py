# mutable.py


def generate_new_list_with(my_list=[], element=None):
    my_list.append(element)
    return my_list


def generate_new_list_with(my_list=None, element=None):
    if my_list is None:
        my_list = []
    my_list.append(element)
    return my_list


def main():
    list1 = generate_new_list_with(element=1)
    print(list1)
    # [1]
    list2 = generate_new_list_with(element=2)
    print(list2)
    # [1, 2]


if __name__ == '__main__':
    main()
