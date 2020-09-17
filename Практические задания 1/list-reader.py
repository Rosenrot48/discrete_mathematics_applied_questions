def reader(array, break_number):
    # --------------------
    # Напишите программу,
    # которая выводит чётные числа из заданного списка и останавливается, если
    # встречает число 237
    # --------------------
    for number in array:
        if number == break_number:
            print('Встретилось блокирующее число: ', break_number)
            break
        else:
            if number % 2 == 0:
                print(number)


reader([2, 1, 3, 4, 5, 2, 1, 312, 321, 237, 123, 4321, 566, 322, 211], 237)
