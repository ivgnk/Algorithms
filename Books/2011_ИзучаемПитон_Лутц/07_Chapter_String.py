"""
05.07.2024-
Глава 7. Strings
"""
from icecream import ic

# стр.208-209
def the_01():
    t = ' rrrff   '
    ic(t.strip(),t.lstrip(),t.rstrip())

    S='123aA'
    ic(list(map(ord, S)))

    r=""" fff  ff   eee   rrrr
        """
    ic(r)

def the_02_split():
    line = 'bob , hacker, 40'
    s = line.split(',')
    print(s)

if __name__ == "__main__":
    the_02_split()