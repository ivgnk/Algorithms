"""
Write a function called repeatStr which repeats the given string string exactly n times.
repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
"""

def repeat_str(rrepeat, sstring):
    return sstring*rrepeat

print(repeat_str(6, "I"))