num1 = int(input("Write the number1 >> "))
num2 = int(input("Write the number2 >> "))

num1_list = []
num2_list = []

def judge(a: int, b: int) -> str:
    for i in range(1, a + 1):
        if a % i == 0:
            num1_list.append(i)
    
    for j in range(1, b + 1):
        if a % j == 0:
            num1_list.append(j)
    
    for k in range(len(num1_list)):
        for t in range(len(num2_list)):
            if num1_list[i] == num2_list[j]:
                return str(False)
            
            else:
                return str(True)

print("두 숫자는 서로수 입니다. >> ", judge(num1, num2))