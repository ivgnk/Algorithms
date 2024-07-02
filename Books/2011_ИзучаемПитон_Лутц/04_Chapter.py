"""
03.07.2024-
Глава 4
"""
from icecream import ic
# Сортировка по ключам: циклы for
def the04_sort_dict_keys():
    """
    Page 140
    """
    d = {'c': 3, 'a': 1, 'b': 2}
    print(d)
    dk=list(d.keys())
    ic(d.keys(),'   ',dk)
    dk.sort()
    ic('after sort = ',dk)
    for key in dk:  # Обход отсортированного списка ключей
        ic(key, '= > ', d[key])
    d2={key:d[key] for key in dk}
    print(d,d2)

def the04_sort_dict_keys2():
    """
    Page 141
    """
    d = {'c': 3, 'a': 1, 'b': 2}
    for key in sorted(d):
        print(key, '= > ', d[key])

def the04_tuple():
    t=(1,2,4)
    t2=t+(5,6)
    print(t2)

def the04_files():
    fn=r'j:\data.txt'
    f = open(fn, 'w')  # Создается новый файл для вывода
    f.write('Hello\n')  # Запись строки байтов в файл
    f.write('world\n')  # В Python 3.0 возвращает количество записанных байтов
    f.close()  # Закрывает файл и выталкивает выходные буферы на диск

    f = open(fn) # ‘r’ – это режим доступа к файлу по умолчанию
    text = f.read() # Файл читается целиком в строку
    print(text) # Вывод, с попутной интерпретацией служебных символов
    t = text.split()
    print(t)

def the04_set():
    X = set('spam')  # В 2.6 и 3.0 можно создавать из последовательностей
    Y = {'h', 'a', 'm'}  # В 3.0 можно определять литералы множеств
    print(X, Y)
    ic(X,Y)
    print('Пересечение', X & Y) # Пересечение {‘a’, ‘m’}
    print('Объединение', X | Y) # Объединение {‘a’, ‘p’, ‘s’, ‘h’, ‘m’}
    print('Разность X - Y', X - Y) # Разность {‘p’, ‘s’}
    print('Разность Y - X', Y - X)


def the04_types():
    i=2
    print(type(i))
    L = [None] * 100
    print(type(L))
    print(type(type(L)))
    ic(type([]))

if __name__ == "__main__":
    the04_types()

# Page 147