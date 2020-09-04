def change_element(input_string):
    # -------------------------------
    # Реализовать программу, которая получает на вход строку, содержащую 2 слова через пробел.
    # На выходе программа должна выводить эти же слова в обратном порядке.
    # При решении не стоит пользоваться условными операторами if и циклами (for, while).
    # -------------------------------
    array = input_string.split(' ')
    if len(array) == 2:
        a = array[0]
        b = array[1]
        print(b + ' ' + a)
    else:
        print('Поддерживается ввод только 2 слов')


change_element('Hello World Santa')
