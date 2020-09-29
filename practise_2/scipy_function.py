from scipy import optimize
import matplotlib.pyplot as plt

a = 2
b = 5


def f(x):
    return (x + a) ** 2 - b


def g(x):
    return abs(f(x))


def calc_min_value(function):
    # Реализовать программу, которая вычисляет минимальное значение функций f(x) и g(x) с использованием пакета
    # scipy.optimize.golden(). Постройте график функций в диапазоне [-10;10] с помощью пакета matplotlib.
    # Функции:
    # f(x) = (x+a)**2 - b
    # g(x) = |f(x)|

    arg_min, val_min, iter_min = optimize.golden(function, brack=(a, b), full_output=True)
    return val_min


def draw_diagram():
    plt.figure(figsize=(16, 9))
    plt.subplot(2, 1, 1)
    plt.plot(range(-10, 10), list(map(f, range(-10, 10))))
    plt.title('График функции g(x)')
    plt.grid()
    plt.ylabel('f(x)')
    plt.xlabel('x')

    plt.subplot(2, 1, 2)
    plt.plot(range(-10, 10), list(map(g, range(-10, 10))))
    plt.title('График функции g(x)')
    plt.grid()
    plt.ylabel('g(x)')
    plt.xlabel('x')
    plt.show()


def scipy_optimize_gloden():
    print('Минимальное значение в функции f(x): ' + str(calc_min_value(f)))
    print('Минимальное значение в функции g(x): ' + str(calc_min_value(g)))


scipy_optimize_gloden()

draw_diagram()
