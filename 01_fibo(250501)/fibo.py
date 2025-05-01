import time

a = int(input("피보나치 수열의 몇번째 숫자를 불러오겠습니까? >> "))
num = []


def fibo(a: int) -> int:
    if a == 1:
        num.append(0)

    else:
        num.append(0)
        num.append(1)

        if a > 2:
            for i in range(a - 2):
                num.append(num[i] + num[i + 1])

    return num


t0 = time.time_ns()

fibo(a)
print(a, "번쨰 숫자는 = ", num[a - 1])

t1 = time.time_ns()
print(f"{(t1 - t0) / 1e6} ms")
