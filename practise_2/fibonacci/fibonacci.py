from fibonacci_core import calculate


def Fibonacci():
    # Реализовать программу для получения N чисел Фибоначчи.
    # Метод вычисления чисел должен располагаться в отдельном пакете.
    # Метод должен использовать генератор для вычисления N чисел.

    size = int(input("Введите размер ряда Фибоначи: "))
    print(next(calculate(size)))


Fibonacci()
