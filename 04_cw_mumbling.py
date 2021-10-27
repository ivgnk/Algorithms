"""
The examples below show you how to write function accum:
Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

# Работа со строками
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
def accum(s):
    n = len(s)
    print(n)
    s3 = ''
    for i in range(n):
        s2=s[i]*(i+1)
        print(i,'  ',s2)
        if (i == (n-1)):
            s3 = s3 + s2.capitalize()
        else:
            s3 = s3 + s2.capitalize() +'-'
    return s3

print(accum('abcd'))
# print(accum('abcd'))