# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
# Пример:
# 6 ->  Да
# 7 -> Да
# 1 -> нет


print('Введите день недели: ')
numDay = int(input())

def NumberDay(numDay):
    if numDay == 1:
        return f'День не является выходным'
    elif numDay == 2:
        return f'День не является выходным'
    elif numDay == 3:
        return f'День не является выходным'
    elif numDay == 4:
        return f'День не является выходным'
    elif numDay == 5:
        return f'День не является выходным'   
    elif numDay == 6:
        return f'Это выходной день'
    elif numDay == 7:
        return f'Это выходной день'
    else:
        return f'Вы введи некорректный номер'
print(NumberDay(numDay))

# Напишите программу, которая принимает на вход координаты точки (X и Y), причем X =/ 0 и Y=/ 0 и выдает номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)
# Пример
# x = 34; y = -30 -> 4
# x = 2; y = 4 -> 4
# x = -34; y = -30 -> 4

print('Введите координату точки X: ')
numX = int(input())
print('Введите координату точки Y: ')
numY = int(input())

def NumCoordinates(numX, numY):
    if numX > 0 and numY > 0:
        return f'Первая четверть'
    elif numX < 0 and numY > 0:
        return f'Втовая четверть'
    elif numX < 0 and numY < 0:
        return f'Третья четверть'
    elif numX > 0 and numY < 0:
        return f'Четвертая четверть'
print(NumCoordinates(numX, numY))
