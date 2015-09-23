# -*- coding: cp1251 -*-

"""****************************************************************************
* Author: Alexander Shcherbakov                                                 
* Written:           23/9/2015
* Execution:         echo 1 2 3 6  | python balance.py
* Execution:         python balance.py < data.txt
* Execution:         python balance.py data.txt
* Execution:(Win)    type data.txt | python balance.py
* Execution:(Lin)    cat data.txt  | python balance.py
* %more data.txt
* 101 102 103 100 5 2 3
* Have tested by Python 2.7 and Python 3.4
*****************************************************************************"""

""" Задание:
2. Баланс весов
Дана конечная последовательность натуральных чисел.
Считая их массами имеющихся в наличии предметов, определить, можно ли все эти
предметы положить на весы так, чтобы весы находились в равновесии. Вывести вариант
расположения.
Определить, можно ли из них отобрать какое-то количество предметов с суммарным
весом 100 (вывести yes или no, в зависимости от результата).

Пример входных данных:
2 4 3 6 5

Пример выходных данных:
2 3 5 - 4 6
no
"""

import itertools
import fileinput

# переводим строку в список чисел
def str_to_num_list(in_str, num_list):    
    str_list = in_str.split()    
    for i in str_list:
        try:
            num_list.append(int(i))
        except:
            print('Wrong input data')
            exit()

# определяем все варианты расположения когда весы в равновесии
# и можно ли из введеных 
def balance(array):
    comb_right = []
    for L in range(0, len(array)+1):
        for subset in itertools.combinations(array, L):
            comb_right.append(subset)

    # оставляем сочетание из n по n что бы проверить ее сумму на равенство 100
    comb_invert = comb_right[:-int((len(comb_right))/2+1):-1]
    comb_right = comb_right[:int(len(comb_right)/2)]
    
    is_summ_100 = False
    
    for i in range(len(comb_right)):        
        if sum(comb_right[i]) == sum(comb_invert[i]):            
            print(str(comb_right[i]).replace('(','').replace(')','').replace(',','') +
                  ' - '+str(comb_invert[i]).replace('(','').replace(')','').replace(',',''))
        if sum(comb_right[i]) == 100 or sum(comb_invert[i]) == 100:
            is_summ_100 = True

    if is_summ_100:
        print('yes')

if __name__ == "__main__":
    # читаем одну строку
    for line in fileinput.input():
        input_line = line
        break    
    
    array = []
    str_to_num_list(input_line, array)
    
    balance(array)  
    
