'''
sorting a list with Selection sort!
'''
import numpy as np

numbers = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(len(numbers)):

    min_value = np.inf #to save minimum value
    idx = -1 #to get the index of the minimun value in the list

    for j in range(i, len(numbers)):

        if min_value > numbers[j]:
            min_value = numbers[j]#replace the min_value
            idx = j#get the index

    numbers[i], numbers[idx] = numbers[idx], numbers[i]#switch the postion

print(numbers)
