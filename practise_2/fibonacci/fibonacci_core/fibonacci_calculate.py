def calculate(size_number):
    if size_number <= 0:
        yield 'Ошибка исполнения. размерность меньше либо равна 0'
    elif size_number == 1:
        yield [0]
    elif size_number == 2:
        yield [0, 1]
    else:
        size_number -= 2
        array = [0, 1]
        while size_number > 0:
            size_number -= 1
            #  Fn-2
            minus_two = array.__getitem__(len(array) - 2)

            # Fn-1
            minus_one = array.__getitem__(len(array) - 1)
            array.append((minus_one + minus_two))
        yield array
