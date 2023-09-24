'''
На основе
Как подсчитать количество одинаковых элементов в списке
https://zdrons.ru/veb-programmirovanie/python-kak-podschitat-kolichestvo-odinakovyh-elementov-v-spiske/

Для подсчета количества элементов в списке используется функция len(),
а для нахождения количества одинаковых элементов — модуль Collections.
Модуль Collections содержит метод Counter(),
который позволяет подсчитать количество вхождений каждого элемента в список.
'''

from collections import Counter

def exaple_001():
    my_list = [1, 1, 2, 3, 3, 3, 4, 4, "строка"]
    n = 3
    count = my_list.count(n)
    print(f'{my_list=}')
    print(f'count({n}), {count=}')

def exaple_002():
    '''
    Поиск количества одинаковых элементов
    '''
    my_list = [1, 2, 3, 1, 4, 2, 1]
    counts = {x: my_list.count(x) for x in my_list}
    print(f'{my_list=}')
    print(f'{counts=}')

    # https://www.techiedelight.com/ru/iterate-over-dictionary-python/
    print(f'\nИтерация по словарю Python, 1 variant')
    for key in counts:
        print(key,' ',counts[key])
    print(f'\nИтерация по словарю Python, 2 variant')
    for key, value in counts.items():
        print(f'{key=}  {value=}')
    #  отсортировать элементы по количеству их вхождений

    print('\n отсортировать элементы counts по количеству их вхождений')
    # Сотрировка по убыванию числа элементов
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    print(f'{sorted_counts=}')

def exaple_003():
    '''
    Использование Counter from collections
    '''
    print('\nИспользование Counter from collections')
    my_list = [1, 2, 3, 1, 4, 2, 1]
    print(f'{my_list=}')
    counts = Counter(my_list)
    print(f'{counts=}')

    # С помощью класса Counter мы можем также рассчитать
    # наиболее часто встречающиеся элементы с помощью метода most_common().
    # Он позволяет нам получить список кортежей, аналогичный примеру выше
    # В результате мы получим список кортежей, отсортированных по количеству вхождений
    most_common = counts.most_common()
    print(f'\n{most_common=}')

def exaple_004():
    '''
    Использование вложенных циклов для перебора
    '''
    count = {}
    list = ['a', 'b', 'a', 'c', 'c', 'a']
    for i in list:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(f'\n{count=}')

def exaple_005():
    '''
    Count и список строк
    '''
    animals = ['cat', 'dog', 'cat', 'lion', 'elephant', 'dog', 'cat']
    print(f'\n{animals=}')
    counts = {animal: animals.count(animal) for animal in animals}
    print(f'\n{counts=}')


if __name__ == "__main__":
    exaple_005()

