'''Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
Пример:  5   1 2 3 4 5    6    -> 5'''

N = int(input('Введите количество элементов в массиве N: '))
array_a = []
for i in range(N):
    X = int(input('Введите число массива: '))
    array_a.append(X)
print('Ваш массив:', *array_a)

number1 = int(X-1)
#number2 = int(X+1)

stoping1 = 0
while stoping1 < 1:
    for i1 in range(N):
        if number1 == array_a[i1]:
            stoping1 = 10 
        else:
            i1 += 1         

print (number1)

''' stoping2 = 0
while stoping2 < 1:
    for i2 in range(N):
        if number2 == array_a[i1]:
            stoping1 = 10 
            break
        else:
            i1 += 1         
print (number1)

if i1 < i2:
    print('Самый близкий элемент массива к числу' , X , 'это число ' , number1)
elif i2 < i1:
    print('Самый близкий элемент массива к числу' , X , 'это число ' , number2)
else:
    print('Самые близкие элементы массива к числу' , X , 'это числа ' , number1, 'и' , number2) '''

