"""
    Обсобые возможности - каррирование и прочее
"""
# Функции Карри в Python
# http://espressocode.top/currying-function-in-python/
# Функциональное программирование на Python. Часть 2. Абстракция и композиция. Функции
# https://devpractice.ru/fp-python-part2-abs-comp-func/
# Замыкания в Python
# https://devpractice.ru/closures-in-python/
# Тонкости использования языка Python: Часть 3. Функциональное программирование
# https://www.ibm.com/developerworks/ru/library/l-python_details_03/
# Теория программирования | Каррирование
# https://www.youtube.com/watch?v=E6T4J2lsQs8

def change(b, c, d):
    def a(x):
        return b(c(d(x)))
    return a

def kilometer2meter(dist):
    "" "Функция, которая преобразует км в м." ""
    return dist * 1000

def meter2centimeter(dist):
    "" "Функция, которая преобразует m в см." ""
    return dist * 100

def centimeter2feet(dist):
    "" "Функция, которая преобразует см в футы." ""
    return dist / 30.48

# x = 4
# def fun():
#         print(x+3)
#     fun()

if __name__ == '__main__':
    # kilometer2meter -> meter2centimeter -> centimeter2feet
    #transform = change(centimeter2feet, meter2centimeter, kilometer2meter)
    #e = transform(565)
    # print(e)
    # Выход: 1853674.5406824148

    n = 3
    def mult(k, mul=n):
        return mul * k
    n = 7
    print(mult(3)) #9
    n = 13
    print(mult(5)) #15
    n = 10
    mult = lambda k, mul=n: mul * k
    print(mult(3))  #30
