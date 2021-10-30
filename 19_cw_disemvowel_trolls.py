"""
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.

Тролли атакуют ваш раздел комментариев! Обычный способ справиться с этой ситуацией - удалить все гласные из комментариев
троллей, нейтрализуя угрозу. Ваша задача - написать функцию, которая принимает строку и возвращает новую строку с
удаленными гласными. Например, строка «Этот сайт для неудачников LOL!» станет "Ths wbst s fr lsrs LL!".
Примечание: для этого ката y не считается гласным.
"""

def disemvowel(string_):
    del_str = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',]
    for i in range(len(del_str)):
        string_ = string_.replace(del_str[i],'')
    return string_

print(disemvowel("This website is for losers LOL!")) # "Ths wbst s fr lsrs LL!"

