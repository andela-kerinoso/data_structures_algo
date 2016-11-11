def bubble_sort(arr_list):
    # For bigO benchmarking
    num_of_comparison = 0
    num_of_exchanges = 0

    for pass_num in range(len(arr_list) - 1, 0, -1):
        for j in range(pass_num):
            num_of_comparison += 1 # For bigO benchmarking
            if arr_list[j] > arr_list[j + 1]:
                arr_list[j], arr_list[j + 1] = arr_list[j + 1], arr_list[j]
                num_of_exchanges += 1 # For bigO benchmarking

    return '%s comparisons and %s exchanges.' % (num_of_comparison, num_of_exchanges) # For bigO benchmarking


def short_bubble_sort(arr_list):
    # For bigO benchmarking
    num_of_comparison = 0
    num_of_exchanges = 0

    exchange = True
    pass_num = len(arr_list) - 1

    while pass_num > 0 and exchange:
        exchange = False
        for j in range(pass_num):
            num_of_comparison += 1 # For bigO benchmarking
            if arr_list[j] > arr_list[j + 1]:
                exchange = True
                arr_list[j], arr_list[j + 1] = arr_list[j + 1], arr_list[j]
                num_of_exchanges += 1 # For bigO benchmarking

        pass_num -= 1

    return '%s comparisons and %s exchanges.' % (num_of_comparison, num_of_exchanges) # For bigO benchmarking


def selection_sort(arr_list):
    # For bigO benchmarking
    num_of_comparison = 0
    num_of_exchanges = 0

    for pass_num in range(len(arr_list) - 1, 0, -1):
        pos_max = 0
        for j in range(1, pass_num):
            num_of_comparison += 1 # For bigO benchmarking
            if arr_list[j] > arr_list[pos_max]:
                pos_max = j

        arr_list[pass_num], arr_list[pos_max] = arr_list[pos_max], arr_list[pass_num]
        num_of_exchanges += 1 # For bigO benchmarking

    return '%s comparisons and %s exchanges.' % (num_of_comparison, num_of_exchanges) # For bigO benchmarking


if __name__ == '__main__':
    import timeit

    unsorted_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted_list = [17, 20, 26, 31, 44, 54, 55, 77, 93]

    sorting_algos = [bubble_sort, short_bubble_sort, selection_sort]

    for sorting_algo in sorting_algos:
        print('{}: {} sec, {}'.format(
                sorting_algo.__name__,
                timeit.timeit(
                    '%s(%s)' % (sorting_algo.__name__, unsorted_list),
                    setup='from __main__ import %s' % sorting_algo.__name__,
                    number=1000
                ),
                sorting_algo([54, 26, 93, 17, 77, 31, 44, 55, 20])
            )
        )
