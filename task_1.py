'''Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке 
вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
Последняя строка содержит число X. 
Пример:  5    1 2 3 4 5    3    -> 1'''

N = int(input('Введите количество элементов в массиве N: '))
array_a = []
for i in range(N):
    X = int(input('Введите число массива: '))
    array_a.append(X)
print('Ваш массив:', *array_a)
print('Последнее число массива' , X , 'повторяется в нём' , array_a.count(X) , 'раз')

