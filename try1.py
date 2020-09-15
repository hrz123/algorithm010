# try1.py

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], ['mike', '1999-01-01', 'male'],
          ['nancy', '2001-02-01', 'female']]


def solve1():
    res = []
    for value in values:
        res.append(dict(zip(attributes, value)))
    return res


def solve2():
    return [dict(zip(attributes, v)) for v in values]


def main():
    print(solve1())
    print(solve2())
    d = {'mike': 10, 'lucy': 2, 'ben': 30}
    print(dict(sorted(d.items(), key=lambda x: x[1], reverse=True)))


if __name__ == '__main__':
    main()
