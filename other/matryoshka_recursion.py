class Matryoshka:

    def __init__(self, size, item=None):
        self.size = size
        self.inner_item = item


def disassemble_matryoshka(matryoshka):
    """Функция разборки матрёшки."""
    inner_item = matryoshka.inner_item
    if inner_item is None:
        print(f'Все матрёшки разобраны! Размер последней матрёшки: {matryoshka.size}')
        return
    print(f'Разобрали матрёшку размера {matryoshka.size}, разбираем дальше!')
    disassemble_matryoshka(inner_item)


if __name__ == '__main__':
    big_matryoshka = Matryoshka('L', Matryoshka('M', Matryoshka('S')))
    disassemble_matryoshka(big_matryoshka)
