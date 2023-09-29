'''
Решение задачи "в лоб"
x**3 + Y**3 = 5
x**2 + Y**2 = 3
'''
import numpy as np
import sys
def p_task_001():
    print('p_task_001')
    xxa = np.arange(-3, 3.01,0.05)
    xxa2 = np.round(xxa, 1)
    nres = 0
    for x in xxa2:
        x2 = x**2
        for y in xxa2:
            x3=x2*x
            y2 = y**2
            y3 = y2*y
            ur1 = round(x3+y3,3)
            ur2 = round(x2+y2,3)
            ur1_tol = 0.001*ur1
            ur2_tol = 0.001*ur2
            # print(f'{x=}  {y=}  {ur1=}  {ur2=}')
            if ((ur1 - 5.00)<ur1_tol) and ((ur2 - 3.00)<ur2_tol):
                print(f'Ответ {x=}  {y=}')
                nres = nres+1
                print(f'{ur1=}   {ur2=}')
    print(f'{nres=} ')
if __name__ == "__main__":
    p_task_001()
