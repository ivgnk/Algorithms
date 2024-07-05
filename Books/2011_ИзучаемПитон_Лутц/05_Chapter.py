"""
05.07.2024
Глава 5
"""
from icecream import ic
from decimal import Decimal
from fractions import Fraction
#--1 Форматы отображения чисел
def the1():
    rr=3.145677
    print(f'{rr=}')
    l=4
    m=5
    print(f'rr={ rr:{l}.{m}f}')
    print('{0:4.2f}'.format(rr))

#--2 Множества, стр 183
def the2():
    s=set([1,'2',3, 4.0, Decimal(1.2), Fraction(2,5), tuple([1,2,3,'r'])])
    print(s)

# стр 189
def the3_set_opreations():
    engineers = {'bob', 'sue', 'ann', 'vic'}
    managers = {'tom', 'sue'}
    ic(engineers, managers)
    ic('bob' in engineers)  # bob – инженер? - True
    ic(engineers & managers)  # Кто одновременно является инженером и менеджером? - {'sue'}
    ic(engineers | managers)  # Все сотрудники из обеих категорий - {'vic', 'sue', 'tom', 'bob', 'ann'}
    ic(engineers - managers)  # Инженеры, не являющиеся менеджерами - {'vic', 'bob', 'ann'}
    ic(managers - engineers)  # Менеджеры, не являющиеся инженерами - {'tom'}
    ic(engineers > managers)  # Все менеджеры являются инженерами? - False (надмножество)
    ic({'bob', 'sue'} < engineers ) # Оба сотрудника - инженеры? - True (подмножество)
    ic((managers | engineers) > managers)  # Множество всех сотрудников является надмножеством менеджеров? - True
    ic(managers ^ engineers)  # Сотрудники, принадлежащие к какой-то одной категории - {'vic', 'bob', 'ann', 'tom'}

def the4_bool():
    ic(isinstance(True, int)) # True
    ic(True == 1)  # True 0 То же самое значение
    ic(True is 1)  # False - Но разные объекты: смотрите следующую главу
    ic(True or False)  # True - То же, что и: 1 or 0
    ic(True + 4)  # 5 - (М-да)

if __name__ == "__main__":
    # the3_set_opreations()
    the4_bool()