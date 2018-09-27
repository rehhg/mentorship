

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
    # reserve space for an empty list
    c = [0] * (len(a) + len(b))
    i = k = n = 0
    # merge two arrays until one of them becomes empty
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    # one of the arrays is empty, but we do not know which of them
    # so we need to go through two cycles again in masses and pull out the last elements
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1

    return c


def merge_sort(arr: list):
    """
    Function which represent merge sorting algorithm
    :param list arr: list to sort
    :return: sorted list
    """
    if len(arr) <= 1:
        return
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    merge_sort(left)
    merge_sort(right)

    merged_arr = merge(left, right)
    arr[:] = merged_arr[:]


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


array = [5, 2, 3, 1, 4, 10, 100, 46, 11, 7]
quick_sort(array)
print(array)
