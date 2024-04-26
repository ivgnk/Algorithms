"""
based on 2023_Алгоритмы С примерами на Python_Хайнеман
p.19-20
"""
from icecream import ic
import time
import random

names=['incr_range','incr_list','random_list','decr_range','decr_list']
n=10_000_000
incr_range=range(1,n,1)
incr_list=list(incr_range)
decr_range=range(n,1,-1)
decr_list=list(decr_range)

# https://ru.stackoverflow.com/questions/565846/Как-создать-список-из-случайных-целых-чисел-используя-списковое-включение
random.seed(124)
rand_list=[random.randint(0,n) for _ in range(n)]
work_lst=[incr_range,incr_list,rand_list,decr_range,decr_list]

for i,dat in enumerate(work_lst):
    start_time = time.time()
    print(start_time)
    r=int(max(dat))
    end_time = time.time()
    print(i,names[i],end_time-start_time)
    print(' ')


