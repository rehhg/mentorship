import random
import timeit


def generate_random_data():
    """
    Generate random list
    :return:
    """
    a = []
    for _ in range(10000):
        a.append(random.randint(0, 1000))
    return a


def bubble_sort(arr):
    """
    Function which represent bubble sort algorithm
    :param list arr: list to sort
    :return: sorted list
    """
    length = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for k in range(length):
            if arr[k] > arr[k+1]:
                sorted = False
                arr[k], arr[k+1] = arr[k+1], arr[k]


def insertion_sort(arr: list):
    """
    Function which represent insertion sort algorithm
    :param list arr: list to sort
    :return: sorted list
    """
    for k in range(1, len(arr)):
        while k > 0 and arr[k-1] > arr[k]:
            arr[k], arr[k-1] = arr[k-1], arr[k]
            k -= 1


def merge(a: list, b: list):
    """
    Function used to merge sorted lists
    :param list a: first list
    :param list b: second list
    :return: merged list
    """
    len_a = len(a)
    len_b = len(b)
    merged_list = []
    i = 0
    k = 0
    while True:
        if i >= len_a:
            merged_list.extend(b[k:])
            return merged_list

        if k >= len_b:
            merged_list.extend(a[i:])
            return merged_list

        if a[i] <= b[k]:
            merged_list.append(a[i])
            i += 1
        else:
            merged_list.append(b[k])
            k += 1


def merge_sort(arr):
    """
    Function which represent merge sorting algorithm
    :param list arr: list to sort
    :return: sorted list
    """
    unsorted_list = arr[:]
    length = len(unsorted_list)
    if length <= 1:
        return unsorted_list
    elif length == 2:
        if unsorted_list[0] > unsorted_list[1]:
            unsorted_list[0], unsorted_list[1] = unsorted_list[1], unsorted_list[0]
        return unsorted_list
    else:
        middle = length // 2
        first_list = merge_sort(unsorted_list[middle:])
        second_list = merge_sort(unsorted_list[:middle])

        return merge(first_list, second_list)


def quick_sort(arr):
    """
    Function which represent quick sorting algorithm
    :param list arr: list to sort
    :return: sorted list
    """
    if len(arr) <= 1:
        return
    # get random barrier
    barrier = arr[0]
    left, middle, right = [], [], []
    for x in arr:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    quick_sort(left)
    quick_sort(right)
    arr[:] = left + middle + right


"""
    Table that shows the execution time of the algorithms (in seconds)
    +----------+-----------+--------+-------+-------+
    | Elements | Insertion | Bubble | Merge | Quick |
    +======================+========+=======+=======+
    | 10       | 0.93      | 1.06   | 7.64  | 8.31  | 
    +----------------------+--------+-------+-------+
    | 100      | 7.03      | 7.06   |131.93 |       |
    +----------------------+--------+-------+-------+
    | 1000     | 87.06     | 95.78  |1712.49|       |
    +----------------------+--------+-------+-------+
    | 10000    | 880.05    |1135.09 | ...   |       |
    +----------------------+--------+-------+-------+
    | 100000   | ...       | ...    | ...   |       |
    +----------------------+--------+-------+-------+
"""

arr = generate_random_data()
t = timeit.Timer("bubble_sort(arr)", "from __main__ import bubble_sort, arr, merge")
print(t.timeit())
