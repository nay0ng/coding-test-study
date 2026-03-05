# Authored by : nayoung918
# Dynamic Array (동적 배열) 구현 연습

arr = []
length = 0      # 실제 데이터가 들어있는 크기
capacity = 0    # 현재 삽입이 가능한 최대 크기


def init():
    global arr, length, capacity
    arr = [None] * 1
    capacity = 1


def expand():
    global arr, capacity
    # TODO: capacity를 2배로 늘리고 기존 데이터를 복사하세요
    pass


def insert(idx, num):
    global arr, length, capacity
    if ???????:
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
