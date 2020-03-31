def True_Array(len_arr, array):
    for i in range(len_arr - 1):
        for j in range(len_arr - 1 - i):
            if array[j] < array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j+1] = buff
    return array


count_arr = int(input())
for k in range(count_arr):
    len_arr = int(input())
    array = list(map(int, input().split()))
    print(*True_Array(len_arr, array))
