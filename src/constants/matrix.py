from domain.Elemento import Elemento


def build_matrix():
    e1 = Elemento(1, 'h', 0)
    e1.conexoes = [5]

    e2 = Elemento(2, 'C', 0)
    e2.conexoes = [2]

    e3 = Elemento(3, 'CO', 1)
    e3.conexoes = [1]

    e4 = Elemento(4, 'OL', 0)
    e4.conexoes = [4]

    e5 = Elemento(5, 'h', 1)
    e5.conexoes = [3, 5]

    e6 = Elemento(6, 'A', 1)

    e7 = Elemento(7, 'h', 0)
    e7.conexoes = [3]

    e8 = Elemento(8, 'C', 1)
    e8.conexoes = [2]

    e9 = Elemento(9, 'OL(a)', 1)
    e9.conexoes = [4]

    e10 = Elemento(10, 'CO(a)', 0)
    e10.conexoes = [1]

    return [
        [e1, e2, e3],
        [e4, e5, e6, e7, e8],
        [e9, e10],
    ]
