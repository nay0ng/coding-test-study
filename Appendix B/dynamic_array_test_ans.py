# Authored by : nayoung918
# Dynamic Array (동적 배열) 구현 - 정답 코드

arr = []
length = 0      # 실제 데이터가 들어있는 크기
capacity = 0    # 현재 삽입이 가능한 최대 크기


def init():
    global arr, length, capacity
    arr = [None] * 1
    capacity = 1


def expand():
    global arr, capacity
    new_arr = [None] * (capacity * 2)
    for i in range(length):
        new_arr[i] = arr[i]
    arr = new_arr
    capacity *= 2


def insert(idx, num):
    global arr, length
    if length == capacity:
        expand()
    for i in range(length, idx, -1):
        arr[i] = arr[i - 1]
    arr[idx] = num
    length += 1


def print_arr():
    print(*arr[:length], end='')
    print(f' | {length} {capacity}\n')


def insert_test():
    print('***** insert_test *****')
    insert(0, 10)   # 10, len = 1, capacity = 1
    print_arr()
    insert(0, 30)   # 30 10, len = 2, capacity = 2
    print_arr()
    insert(1, 20)   # 30 20 10, len = 3, capacity = 4
    print_arr()
    insert(3, 40)   # 30 20 10 40, len = 4, capacity = 4
    print_arr()
    insert(1, 50)   # 30 50 20 10 40, len = 5, capacity = 8
    print_arr()
    insert(0, 15)   # 15 30 50 20 10 40, len = 6, capacity = 8
    print_arr()


init()
insert_test()
