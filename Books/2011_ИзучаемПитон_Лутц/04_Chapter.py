"""
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

if __name__ == "__main__":
    the04_sort_dict_keys2()

# Page 143