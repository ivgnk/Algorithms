"""
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.

Простой, учитывая строку слов, возвращает длину самого короткого слова (слов).
Строка никогда не будет пустой, и вам не нужно учитывать разные типы данных.

https://www.cyberforum.ru/python-beginners/thread1537406.html
"""
import re

def find_short(s):
    l = len(s)
    s2=re.split('\s+', s)
    # print(s2)

    l =len(min(s2, key=len))
    # print(l)
    return l # l: shortest word length

print(find_short('aa bbb cccc ddd ee f'))


