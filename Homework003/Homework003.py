# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число

lst = [0, 1, 2, 3, 4, 5]
print(lst)
A = int(input('Input number: '))

def FindNumberOfList(A, lst):
    if A in lst:
        print('Такое число есть в списке.')
    else:
        print('Такого числа в списке нет.')

FindNumberOfList(A, lst)

# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что ее нет
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"] -> ищем "qwe" -> ответ 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"] -> ищем "йцу" -> ответ 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"] -> ищем "йцу" -> ответ -1
# список: ["123", "234", 123, "567"] -> ищем "123" -> ответ -1
# список: [] -> ищем "123" -> ответ -1

list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
list4 = ["123", "234", 123, "567"]
list5 = []

pos1 = "qwe"
pos2 = "йцу"
pos3 = "йцу"
pos4 = "123"
pos5 = "123"

print("Выберите номер списка: ")
A = int(input())
if A == 1:
    print(list1)
    print("Будем искать второе вхождение qwe")
    pos = pos1
    list = list1
elif A == 2:
    print(list2)
    print("Будем искать второе вхождение йцу")
    pos = pos2
    list = list2
elif A == 3:
    print(list3)
    print("Будем искать второе вхождение йцу")
    pos = pos3
    list = list3
elif A == 4:
    print(list4)
    print("Будем искать второе вхождение 123")
    pos = pos4
    list = list4
elif A == 5:
    print(list5)
    print("Будем искать второе вхождение 123")
    pos = pos5
    list = list5

def FindPosOfEl(lst:list):
    count = 0
    poz = pos
    for i in range(0, len(lst)):
        if lst[i] == poz:
            count+=1
            if count == 2:
                print("Позиция второго вхождения =" )
                print(i)
                break
    else:
        print("Такого числа нет")

FindPosOfEl(list)


