"""
Тестирование вывода на печать и форматирования
"""
import sys

def print1() -> None:
    """
    различные разделители при выводе и перевод строки после
    """
    a=10; b=20
    print(a, b, sep='***', end ='')
    print(a, b, sep='---')
    print(b, a, sep=' ',end='\n')
    print(b, a)
    sys.stdout.write(str(a+b)) # sys.stdout.write - только строки

def print2_get_doc() -> None:
    """
    Печать помощи и строк документаций
    """
    # print(help(sys))
    # print(sys.__doc__)
    # print(sys.exit.__doc__)
    # print(dir(sys))
    print(dir())


def print3():
    """
    Форматирование строк для вывод
    """


