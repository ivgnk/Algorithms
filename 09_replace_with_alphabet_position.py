"""
Fundamentals
you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.

от вас требуется заменить каждую букву в строке на ее позицию в алфавите.
Если что-то в тексте не является буквой, игнорируйте это и не возвращайте.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

Таблица Символов
http://microsin.net/adminstuff/others/ascii-charset.html
"""

def alphabet_position(s):
    n = len(s)
    res_str = ''
    for i in range(n):
        s2 = s[i]
        if s2.isalpha():
            code = ord(s2)
            if s2.isupper(): code2 = code - 64
            if s2.islower(): code2 = code - 96
            res_str = res_str + str(code2) + ' '
    res_str = res_str.strip()
    return res_str

print(alphabet_position("The sunset sets at twelve o' clock."))