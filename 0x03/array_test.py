def insert(idx, num, arr, arr_len):
    arr.append(arr[-1])
    for i in range(arr_len-1, idx-1, -1):
        arr[i+1] = arr[i]
    arr[idx] = num

def erase(idx, arr, arr_len):
    for i in range(idx+1, arr_len):
        arr[i-1] = arr[i]
    del arr[-1]

arr = [10, 50, 40, 30, 70, 20]
arr_len = 6
insert(3, 60, arr, arr_len)
arr_len += 1
print(arr, arr_len)
erase(4, arr, arr_len)
arr_len -= 1
print(arr, arr_len)