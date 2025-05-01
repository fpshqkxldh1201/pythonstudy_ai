import time

num = int(input("Enter: "))

table = {1: 0, 2: 1}


def fibo(num: int) -> int:
    if num in table:
        return table[num]

    out = fibo(num - 2) + fibo(num - 1)
    if out not in table:
        table[num] = out

    return out


t0 = time.time_ns()

print(fibo(num))

t1 = time.time_ns()
print(f"{(t1 - t0) / 1e6} ms")
