num = int(input("Enter: "))


def fibo(num: int) -> int:
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibo(num - 2) + fibo(num - 1)  # recursive function


answer = fibo(num)

print(answer)


# 재귀함수 시간목잡도 = O(2^n)
# 단점으로 결과가 나오는 시간이 너무 오래 걸림
