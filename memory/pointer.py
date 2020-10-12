def change_x(x):
    x.append(4)


class Car:

    def __init__(self, year):
        self.year = year

    def __repr__(self):
        return f'Car({self.year})'


if __name__ == '__main__':
    a = Car(2010)
    b = a

    c = [1, 2, 3, 4]
    print(id(c))
    c.append(5)
    print(id(c))

    # print(id(a))
    # print(id(b))

    a.year = 2011

    print(a)
    print(b)
