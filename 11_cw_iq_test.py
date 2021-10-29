"""
Fundamentals
Bob is preparing to pass IQ test. The most frequent task in this test is
to find out which one of the given numbers differs from the others.
Bob observed that one number usually differs from the others in evenness.
Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness,
and return a position of this number.
! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

Боб готовится сдать тест на IQ. Наиболее частая задача в этом тесте - выяснить, какое из заданных чисел отличается от других.
Боб заметил, что одно число обычно отличается от других четноностью. Помогите Бобу - чтобы проверить его ответы,
ему нужна программа, которая среди заданных чисел найдет одно, отличающееся по четности, и вернет позицию этого числа.
! Имейте в виду, что ваша задача - помочь Бобу пройти настоящий тест на IQ,
что означает, что индексы элементов начинаются с 1 (а не с 0).

Examples:
iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even
iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd
"""

def iq_test(numbers):
    # перевод строки в список, в списке минимум три значения
    # https://pythonim.ru/string/preobrazovanie-stroki-v-spisok-v-python
    list_s = numbers.split()
    list_n = []; list_b = []
    list_odd = [0, 0] # число четных и нечетных элементов
    for el in list_s:
        num = int(el)
        list_n.append(num)
        num2 = num % 2 # остаток от деления на 2
        res = (num2 == 0) # определяем четность
        list_b.append(res)
        list_odd[num2] = list_odd[num2] +1 # считаем четные и нечетные

    # print(list_s);     print(list_n);     print(list_b);   print(list_odd)

    for i, el in enumerate(list_b):
        # print(i,'  ',el,' ',int(el))
        if list_odd[int(not el)] == 1:
            return i+1 # потому что в задаче нумерация элементов с 1

numbers = "2 4 7 8 10"
numbers = "7 4 2 8 10 102"
numbers = "2 4 7 8 10 102"
numbers = "1 2 1 1"
print(' Result = ', iq_test(numbers))

