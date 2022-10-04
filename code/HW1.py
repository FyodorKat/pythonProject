import numpy as np
from numpy import dot
from numpy.linalg import norm
#Задача 1
#N хоббитов делят K кусков эльфийского хлеба поровну, не делящийся нацело остаток остается в корзинке у Сэма.
# Напишите функцию, которая принимает на вход параметры N и K и возвращает два числа: x - cколько кусков эльфиского
# хлеба достанется каждому хоббиту, и y - сколько кусков остаётся в корзинке.
def share_bread(N, K):
    each_bread = (K // N)
    remains = (K % N)
    return each_bread, remains

# если в функции всё верно, то после выполнения этой строчки, не должно выскакивать ошибок
assert share_bread(N=3, K=14) == (4, 2)

print(share_bread(3, 14))

#Задача 2
#В копях Мории хоббиты нашли стену, на которой высечены разные натуральные числа. Согласно древним сказаниям,
# это даты сражений. Хоббиты знают, что сражения происходили только по високосным годам.
# Помогите хоббитам определить, является ли год с данным числом датой великого сражения.
# Если это так, то верните строку "YOU SHALL PASS", иначе верните "YOU SHALL NOT PASS".
# Напомним, что в соответствии с хоббитским календарем, год является високосным, если его номер кратен 4,
# но не кратен 100, а также если он кратен 400.

def leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return 'YOU SHALL PASS'
    else:
        return 'YOU SHALL NOT PASS'

print(leap_year(year=5))
assert leap_year(5) == 'YOU SHALL NOT PASS'

#Для могущественного магического ритуала Гендальфу необходимо быстро подсчитывать площадь своего амулета,
# который умеет менять размеры. Известно, что амулет имеет форму треугольника и Гендальф знает длину
# каждой из сторон. Напишите функцию, которая считает площадь амулета по трем сторонам.
#Подсказка: используйте формулу Герона

def amulet_area(a, b, c):
    p = (a + b + c)/2
    S = np.sqrt(p*(p - a)*(p - b)*(p - c))
    return S

assert amulet_area(3, 4, 5) == 6
print(amulet_area(3, 4, 5))

#Хоббиты собираются пешком идти до Мордора и им нужно подсчитать расстояние, которое им предстоит пройти.
# Хоббиты смогли вспомнить сразу несколько метрик расстояния: евклидово, манхэттена и косинусное,
# так что ваша задача - напистаь функцию под каждую из них. Важное условие - используйте только базовые
# функции numpy для решения.
def cal_euclidean(a, b):
    square = np.square(a - b)
    sum_ = np.sum(square)
    distance = np.sqrt(sum_)
    return distance

def cal_manhattan(a, b):
    abs_ = abs(a - b)
    distance = np.sum(abs_)
    return distance

def cal_cosine(a, b):
    distance = dot(a, b)/(norm(a)*norm(b))
    return distance

a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))

#Ну и напоследок, еще немного практики numpy, без которой не обходится ни один хоббит.
#Создайте случайный array (np.random.rand()) длинной 100. Преобразуйте его так, чтобы
#Максимальный элемент(ы) был равен 1
#Минимальный элемент(ы) был равен 0
#Остальные элементы в итнтервале от 0 до 1 остаются прежними

my_array = np.random.rand(100)
print(np.max(my_array), np.min(my_array))
print(my_array)

my_array = np.random.randint(0, 50, size=(5,6))
selected_column = my_array[:, np.argmax(my_array.max(axis=0))]
print('Shape: ',my_array.shape)
print('Array')
print(my_array)
print(selected_column)

#Напишите функцию, которая принимает на вохд матрицу (array) X и возвращает все её уникальные строки
# в виде новой матрицы.
def get_unique_rows(X):
    X_unique = np.unique(X, axis=0)
    return X_unique

X = np.random.randint(4, 6, size=(10,3))
print(X)
print('Unique rows: ',get_unique_rows(X))