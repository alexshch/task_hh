# -*- coding: cp1251 -*-

"""****************************************************************************
* Author: Alexander Shcherbakov                                                 
* Written:           23/9/2015
* Execution:         python min_dist.py < test.txt
* Execution:         python min_dist.py test.txt
* Execution:(Win)    type test.txt | python min_dist.py
* Execution:(Lin)    cat test.txt  | python min_dist.py
* Have tested by Python 2.7 and Python 3.4
*****************************************************************************"""

""" 1. Минимальное расстояние
Дан набор из N точек на плоскости (для простоты можно считать, что у всех
точек целочисленные координаты). Найдите минимальное расстояние между двумя
точками из этого набора.

Пример входных данных:
10 10
20 10
20 15

Пример выходных данных:
5
"""
import itertools
import fileinput

# возвращает растояние между двумя точками
# points -  кортеж из двух точек
def dist(points):
    return abs(points[0] - points[1])

# возвращает минимальное растояние
# distances - кортеж растояний
def min_dist(distances):
    min_dst = distances[0]
    for i in distances:
        if i is not 0 and i < min_dst:
            min_dst = i
    return min_dst

# возвращает кортеж растояний
# points -  кортеж с точками
def points_to_dist(points):    
    ret_dist = []
    for i in points:
        dst = dist(i)
        ret_dist.append(dst)
    return tuple(ret_dist)

# возвращает кортеж состоящий из двух точек
# in_str - строка вида '11 25'
def line_to_points_tuple(in_str):
    points = []
    str_list = in_str.split()
    if len(str_list) is not 2:
        print('Wrong input data')
        exit()        
    for i in str_list:
        try:
            points.append(int(i))
        except:
            print('Wrong input data')
            exit()
    points = tuple(points)
    return points

if __name__ == "__main__":
    points_array = []
    for line in fileinput.input():
        pair_pts = line_to_points_tuple(line)
        points_array.append(pair_pts)

    distances = points_to_dist(points_array)
    min_distance = min_dist(distances)

    print(min_distance)
