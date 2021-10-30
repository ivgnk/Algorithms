"""
Complete the solution so that the function will break up camel casing, using a space between words.
Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
    sres = ''
    if s == "":
        return sres
    else:
        for chr_ in s:
            if chr_.isupper():
                sres = sres + ' '
            sres = sres + chr_
        return sres

s = "identifier"
s = ""
s = "camelCasing"
s = "breakCamelCase"

print(solution(s))
