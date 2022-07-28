# Задайте натуральное число N, Напишите прогрмму, которая составит список простых множителей числа N.

print("Введите целое число: ")
N = int(input())

def Multiplier(n):
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    return lst

print(Multiplier(N))

