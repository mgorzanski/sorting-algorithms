# This module provides popular sorting algorithms: Bubble sort, Bucket sort, Heap sort, Merge sort, Insertion sort,
# Selection sort, Counting sort and Quick sort


""" Heap sort """


def validate_max_heap(list: list, heap_size: int, parent_index: int) -> None:
    """
    Check if a heap is well-organized

    :param list: heap
    :param heap_size: size of a heap
    :param parent_index: index of the element from which it will be checked
    """
    # heap size is required in stripping heap that is removing subsequent organized elements from heap
    max_element_index = parent_index
    left_child_index = parent_index * 2 + 1
    right_child_index = parent_index * 2 + 2

    if left_child_index < heap_size and list[left_child_index] > list[max_element_index]:
        max_element_index = left_child_index
    if right_child_index < heap_size and list[right_child_index] > list[max_element_index]:
        max_element_index = right_child_index
    # if a change has happened the child is swapped with parent and then again we are checking if heap is well-organized
    # for children of the same parent but with a new value
    if max_element_index != parent_index:
        list[max_element_index], list[parent_index] = list[parent_index], list[max_element_index]
        # max_element_index is a new parent of this subset
        validate_max_heap(list, heap_size, max_element_index)


def heap_sort(list_to_sort: list) -> None:
    """
    Sorts a list using heap sort algorithm.

    :param list_to_sort: list to sort
    """
    n = len(list_to_sort)

    # index of last parent in a binary tree is - number of elements / 2 - 1 (we are checking if a heap is well-organized
    # starting from the last parent)
    for i in range(n // 2 - 1, -1, -1): # while i is greater or equal zero
        validate_max_heap(list_to_sort, n, i)

    # validation starts from the last root (on the bottom)
    for i in range(n - 1, 0, -1):
        # swap of the last element (i) with the first element (root), that is the greatest
        list_to_sort[0], list_to_sort[i] = list_to_sort[i], list_to_sort[0]
        n -= 1  # removal of the last element, that has been swapped
        # and also it is now ordered (it is the last element of a list)
        validate_max_heap(list_to_sort, n, 0)  # check again if a heap is well-organized starting from the top


""" Merge sort """


def merge_sets(start_index: int, old_set_start_index: int, end_index: int, list:list) -> None:
    """
    Merges sub-sets.

    :param start_index: start index of the first set
    :param old_set_start_index: start index of the second set
    :param end_index: end index of the second set
    :param list: list on which merging happens
    """
    p = list[0:end_index + 1]
    i1 = start_index
    i2 = old_set_start_index
    for i in range(start_index, end_index + 1):
        if (i1 == old_set_start_index) or (i2 <= end_index and list[i1] > list[i2]):
            p[i] = list[i2]
            i2 += 1
        else:
            p[i] = list[i1]
            i1 += 1
    for i in range(start_index, end_index + 1):
        list[i] = p[i]


def merge_sort(start_index: int, end_index: int, list_to_sort: list) -> None:
    """
    Sorts a list using merge sort algorithm.

    :param list_to_sort: list to sort
    :param start_index: start index of a list
    :param end_index: end index of a list
    """
    old_set_start_index = start_index + end_index + 1 // 2
    if old_set_start_index - start_index > 1:
        merge_sort(start_index, old_set_start_index - 1, list_to_sort)
    if end_index - old_set_start_index > 0:
        merge_sort(old_set_start_index, end_index, list_to_sort)
    merge_sets(start_index, old_set_start_index, end_index, list_to_sort)


""" Quick sort """


def quick_sort(list_to_sort: list, left_index: int, right_index: int) -> None:
    """
    Sorts a list using quick sort algorithm.

    :param list_to_sort: list to sort
    :param left_index: first index of a list
    :param right_index: last index of a list
    """
    i = (left_index + right_index) // 2  # searches for elements that are less than pivot
    pivot = list_to_sort[i]
    list_to_sort[i] = list_to_sort[right_index]  # swap pivot with last element of list to sort
    j = left_index  # remember's position where the next swapped element is going to
    # appear (at the end it tells where pivot will appear)
    for i in range(left_index, right_index):
        if list_to_sort[i] < pivot:
            list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
            j += 1
    list_to_sort[right_index] = list_to_sort[j]
    list_to_sort[j] = pivot
    if left_index < j - 1:
        quick_sort(list_to_sort, left_index, j - 1)
    if j + 1 < right_index:
        quick_sort(list_to_sort, j + 1, right_index)


""" Insertion sort """


def insertion_sort(n: int, list_to_sort: list) -> None:
    """
    Sorts a list using insertion sort algorithm.

    :param n: length of a list to sort
    :param list_to_sort: list to sort
    """
    for j in range(n - 2, -1, -1):  # from next to last to 0 included
        x = list_to_sort[j]
        i = j + 1
        # check if any of next elements is smaller than selected (j) element and if it is change the order (make space)
        # for it
        while i < n and x > list_to_sort[i]:
            list_to_sort[i - 1] = list_to_sort[i]
            i += 1
        # insert selected element to a new position
        list_to_sort[i - 1] = x


""" Counting sort """


def counting_sort(n: int, list_to_sort: list) -> None:
    """
    Sorts a list using selection sort algorithm.

    :param n: length of a list
    :param list_to_sort: list to sort
    """
    max_val = max(*list_to_sort)
    min_val = min(*list_to_sort)
    start_min = 0
    if min_val < 0:
        start_min = min_val
        for i in range(n):
            list_to_sort[i] -= min_val
        max_val -= min_val
        min_val = 0

    counters = [0] * (max_val + 1)
    for i in range(n):
        counters[list_to_sort[i]] += 1

    j = 0
    i = min_val
    while i <= max_val:
        while counters[i] != 0:
            list_to_sort[j] = i
            j += 1
            counters[i] -= 1
        i += 1

    if start_min < 0:
        for i in range(n):
            list_to_sort[i] += start_min


""" Selection sort """


def selection_sort(n: int, list_to_sort: list) -> None:
    """
    Sorts a list using selection sort algorithm.

    :param n: length of a list
    :param list_to_sort: list to sort
    """
    for j in range(0, n - 1):  # search through list to next to last element (because it will be automatically sorted)
        p_min = j  # set position of minimum value in list to be the same as current element (see below)
        for i in range(j + 1, n):  # search smaller value in remaining elements
            if list_to_sort[i] < list_to_sort[p_min]:
                p_min = i  # set the minimum value position
        # swap current element with a smaller (outside of FOR loop!)
        list_to_sort[j], list_to_sort[p_min] = list_to_sort[p_min], list_to_sort[j]


""" Bucket sort """


def bucket_sort(n: int, list_to_sort: list) -> None:
    """
    Sorts a list using bucket sort algorithm.

    :param n: length of a list
    :param list_to_sort: list to sort
    """
    min_value = min(*list_to_sort)
    max_value = max(*list_to_sort)
    counters = [0] * (max_value + 1)
    for i in range(n):
        counters[list_to_sort[i]] += 1
    j = 0
    for i in range(min_value, max_value + 1):
        while counters[i] > 0:
            list_to_sort[j] = i
            counters[i] -= 1
            j += 1


""" Bubble sort """


def bubble_sort(n: int, list_to_sort: list) -> None:
    """
    Sorts a list using bubble sort algorithm.

    :param n: length of a list
    :param list_to_sort: list to sort
    """
    for j in range(n - 2, -1, -1):
        change = False
        for i in range(0, j + 1):
            if list_to_sort[i] > list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                change = True
        if not change:
            break
