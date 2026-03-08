def func1(N):
    result = 0
    for n in range(1, N+1):
        if n % 3 == 0 or n % 5 == 0:
            result += n
    return result

def func2(arr, N):
    for idx, n in enumerate(arr):
        remainder = 100 - n
        if remainder in arr and arr.index(remainder) != idx:
            return 1
    return 0

def func3(N):
    import math
    x = math.isqrt(N)
    if int(x) ** 2 == N:
        return 1
    else:
        return 0
    
    '''
    시간 복잡도는 1, 2, 이렇게 가다가 루트 N까지 갈거이기 때문에 시간 복잡도는 O(루트 n이다.)
    for i in range(1, N+1): 
        if i * i == N:
            return 1
    return 0
    '''

def func4(N):
    result = 1
    while result * 2 <= N:  # 조건 안 맞으면 즉시 탈출!
        result *= 2
    return result

    '''
    제곱되면서 수가 증가하기 때문에 O(log N)가 된다.
    '''

def test1():
    print("****** func1 test ******")
    n   = [16, 34567, 27639]
    ans = [60, 278812814, 178254968]
    for i in range(3):
        result = func1(n[i])
        print(f"TC #{i}")
        print(f"expected : {ans[i]} result : {result}", end="")
        if ans[i] == result:
            print(" ... Correct!")
        else:
            print(" ... Wrong!")
    print("*************************\n")

def test2():
    print("****** func2 test ******")
    arr = [[1, 52, 48], [50, 42], [4, 13, 63, 87]]
    n   = [3, 2, 4]
    ans = [1, 0, 1]
    for i in range(3):
        result = func2(arr[i], n[i])
        print(f"TC #{i}")
        print(f"expected : {ans[i]} result : {result}", end="")
        if ans[i] == result:
            print(" ... Correct!")
        else:
            print(" ... Wrong!")
    print("*************************\n")

def test3():
    print("****** func3 test ******")
    n   = [9, 693953651, 756580036]
    ans = [1, 0, 1]
    for i in range(3):
        result = func3(n[i])
        print(f"TC #{i}")
        print(f"expected : {ans[i]} result : {result}", end="")
        if ans[i] == result:
            print(" ... Correct!")
        else:
            print(" ... Wrong!")
    print("*************************\n")

def test4():
    print("****** func4 test ******")
    n   = [5, 97615282, 1024]
    ans = [4, 67108864, 1024]
    for i in range(3):
        result = func4(n[i])
        print(f"TC #{i}")
        print(f"expected : {ans[i]} result : {result}", end="")
        if ans[i] == result:
            print(" ... Correct!")
        else:
            print(" ... Wrong!")
    print("*************************\n")

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()