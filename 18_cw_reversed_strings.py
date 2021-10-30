"""
Reversed Strings

Complete the solution so that it reverses the string passed into it.
Завершите решение так, чтобы оно перевернуло переданную в него строку.
'world'  =>  'dlrow'
'word'   =>  'drow'
"""

def solution(sstring:str):
    # S[i:j:step]	Извлечение среза
    s=''
    for i in range(len(sstring)-1, -1, -1):
        s = s + sstring[i]
    return s

print(solution(''))
print(solution('s'))
print(solution('sstring'))
