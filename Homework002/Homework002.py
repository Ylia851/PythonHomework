# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# Пример:
# 6782 -> 23
# 0.56 -> 11


A = input("Input the number: ")

def Sum(A):
    sum = 0
    for i in A:
        if i!=".":
            if i!=",":
                sum = sum + int(i)
    return sum
     
print(f"The sum of the {A} is: ",)
print(Sum(A))

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
# Пример:
# пусть N  = 4, тогда [1, 2, 6, 24]  (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input("Input integer number: "))

def Mult(N):
    multiplication = 1
    for i in range(1, N+1):
        multiplication *=i
    return multiplication

print(f'Set of products of numbers from 1 to {N} = ', end = '')
for i in range(1, N+1):
    if i <= N:
        print(f"The multiplication from 1 to {i} is: ",)
        print(Mult(i))
        i+=1