"""
Тестирование работы со словарями в Python
"""
# Python. Урок 9. Словари (dict)
# https://devpractice.ru/python-lesson-9-dict/

def dict_test() -> None:
    d: dict = dict()
    d = {"position":2}
    #print(d["position"])
    #print(d)
    e = d
    d = {"rition": 5}
    print(d)
    print(e)




