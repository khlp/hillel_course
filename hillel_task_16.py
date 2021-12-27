unsorted_list = [3, 1, 0, 9, 4, 13, 2]
sorted_list = []

def data_sorting():
    while unsorted_list:
        minimum = unsorted_list[0]
        for item in unsorted_list:
            if item < minimum:
                minimum = item
        sorted_list.append(minimum)
        unsorted_list.remove(minimum)
    print(sorted_list)

data_sorting()