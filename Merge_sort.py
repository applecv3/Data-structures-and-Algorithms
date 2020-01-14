'''
sort a list of numbers with merge sort
'''


numbers = [3, 7, 8, 1, 5, 9, 6, 10, 2, 4]


def merge_sort(number_list):

    if len(number_list) == 1:#when the list has only one number return!
        return number_list

    center = len(number_list) // 2#to divide the list into two groups!

    group1 = merge_sort(number_list[:center])#recursion! to reach until it gets available to sort!
    group2 = merge_sort(number_list[center:])

    merged_list = []

    while len(group1) != 0 and len(group2) != 0:#compare the first value in each group and get the smaller one

        if group1[0] < group2[0]:
            merged_list.append(group1.pop(0))
        else:
            merged_list.append(group2.pop(0))

    while group1:#the rest of values when it has no values in this ends
        merged_list.append(group1.pop(0))
    while group2:
        merged_list.append(group2.pop(0))

    return merged_list


print(merge_sort(numbers))
