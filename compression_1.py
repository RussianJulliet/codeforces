len_arr = int(input())
array = list(map(int, input().split()))


def min1_array(array):
    delete = 0
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            array[i] += 1
            array[i + 1] = 0
            delete += 1
    # print(array)
    # print('*', delete)
    if delete != 0:
        for i in range(len(array)):
            if array[i] == 0:
                for k in range(i, len(array) - 1):
                    array[k] = array[k + 1]
        for t in range(delete):
            array.pop()
        # print(array)
        return min1_array(array)
    if delete == 0:
        return len(array)


print(min1_array(array))


