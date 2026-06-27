def func2(arr, n):
    num_list = [0] * 101
    for i in arr:
        num_list[i] = 1
    for idx, n in enumerate(num_list):
        if n == 1 and num_list[100-idx] == 1:
            return 1
    return 0

def func2_ans(arr, n):
    occur = [0] * 101
    for i in arr:
        if occur[100 - i] == 1:  # 먼저 짝 확인
            return 1
        occur[i] = 1             # 없으면 저장
    return 0


print(func2([4, 13, 63, 87], 4))