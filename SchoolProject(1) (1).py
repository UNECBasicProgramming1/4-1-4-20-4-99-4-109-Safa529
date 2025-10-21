import math

n1 = float(input('Введите вещественное число: ')) #4.1
n2 = float(input('Введите вещественное число: '))
if n1 > n2:
    print(f'Наибольшое число {n1}')
    print(f'Наименьшее число {n2}')
else:
    print(f'Наибольшое число {n2}')
    print(f'Наименьшее число {n1}')

x = float(input('Введите число: ')) #4.2
if x > 0:
    y = (math.sin(x))**2
    print(f'Значение {y}')
else:
    y = 1 - 2 * math.sin(x**2)
    print(f'Значение {y}')

x = float(input('Введите число: ')) #4.3
if x > 0:
    y = math.sin(x**2)
    print(f'Значение {y}')
else:
    y = 1 + 2 * (math.sin(x))**2
    print(f'Значение {y}')

x = float(input('Введите число: ')) #4.4
if x > 4:
    print('Вторая область')
elif x < 4:
    print('Первая область')

y = float(input('Введите число: ')) #4.5
if y > 3:
    print('Первая область')
elif y < 3:
    print('Вторая область')

x = float(input('Введите значение: ')) #4.6
if x < 2:
    y = x 
    print(f'Заначение y - {y}')
elif x == 2:
    y = x
    print(f'Значение y - {y}')
else:
    print('Такого значения нет')

x = float(input('Введите значение: ')) #4.7
if math.sin(x) < 0:
    k = x**2
else:
    k = abs(x)

if k < x:
    f = k * x
    print(f'Значение функции - {f}')
else:
    f = k + x
    print(f'Значение функции - {f}')

x = float(input('Введите значение: ')) #4.8
if math.sin(x) >= 0:
    k = x**2
else:
    k = abs(x)

if x < k:
    f = abs(x)
    print(f'Значение функции - {f}')
else:
    f = k * x
    print(f'Значение функции - {f}')

n1 = float(input(f'Введите вещественное число: ')) #4.9
n2 = float(input(f'Введите вещественное число: '))
if n1 > n2:
    print(f'Наибольшое число - {n1}')
    print(f'Наименьшее число - {n2}')
else:
    print(f'Наибольшое число - {n2}')
    print(f'Наименьшее число - {n1}')

ras1 = float(input('Введите расстояние в км: ')) #4.10
ras2 = float(input('Введите расстояние в футах: '))
if ras1 > (ras2 * 0.3048):
    print(f'Наиболшое расстояние - {ras1}')
    print(f'Наиименьшее растояние - {ras2}')
elif (ras2 * 0.3048) > ras1:
    print(f'Наибольшое расстояние - {ras2}')
    print(f'Наименьшее растояние - {ras1}')
else:
    print(f'Одиннакого')

sk1 = float(input('Введите скорость в (км в час): ')) #4.11
sk2 = float(input('Введите скорость в (метр в секунду): '))
if sk2 > (sk1 / 3.6):
    print(f'Наиболшая скорость - {sk2}')
    print(f'Наиименьшая скорость - {sk1}')
elif sk2 < (sk1 / 3.6):
    print(f'Наибольшая скорость - {sk1}')
    print(f'Наименьшая скорость - {sk2}')
else:
    print(f'Одиннакого')

r = float(input('Введите значение радиуса: ')) #4.12
a = float(input('Введите значение стороны квадрата'))
S1 = math.pi * r**2
S2 = a**2
if S1 > S2:
    print(f'Площадь круга больше - {S1}')
    print(f'Площадь квадрата меньше - {S2}')
elif S1 < S2:
    print(f'Площадь квадрата больше - {S2}')
    print(f'Площадь круга меньше - {S1}')
else:
    print('Одиннакого')

m1 = float(input('Введите значение массы первого: ')) #4.13
m2 = float(input('Введите значение массы второго: '))
V1 = float(input('Введите значение объема первого: '))
V2 = float(input('Введите значение объема второго: '))
p1 = m1 / V1
p2 = m2 / V2
if p1 > p2:
    print(f'Плотность первого больше - {p1}')
    print(f'Плотность второго меньше - {p2}')
elif p1 < p2:
    print(f'Плотность первого меньше - {p1}')
    print(f'Плотность второго большее - {p2}')
else:
    print('Одиннакого')

R1 = float(input('Введите значение сопротивления первого: ')) #4.14
R2 = float(input('Введите значение сопротивления второго: '))
U1 = float(input('Введите значение напряжение первого: '))
U2 = float(input('Введите значение напряжение второго: '))
I1 = R1 * U1
I2 = R2 * U2
if I1 > I2:
    print(f'Сила тока первого больше - {I1}')
    print(f'Сила тока второго меньше - {I2}')
elif I1 < I2:
    print(f'Сила тока первого меньше - {I1}')
    print(f'Сила тока второго большее - {I2}')
else:
    print('Одиннакого')

a = float(input('Введите значение старщего коэффицента: ')) #4.15
b = float(input('Введите значение среднего коэффицента: '))
c = float(input('Введите значение свободного члена: '))
if a != 0:
    D = math.sqrt(b**2 - 4 * a * c)
    if D > 0:
        print('Уравнение имеет два разных корня')
    elif D == 0:
        print('Уравнение имеет один или два равных корня')
    else:
        print('Не имеет корней')
else:
    print('Старший коэффицент не может быть равна нулю')

a = float(input('Введите значение старщего коэффицента: ')) #4.16
b = float(input('Введите значение среднего коэффицента: '))
c = float(input('Введите значение свободного члена: '))
if a != 0:
    D = math.sqrt(b**2 - 4 * a * c) 
    if D > 0:
        x1 = (-b + D) / 2 * a
        x2 = (-b - D ) / 2 * a
        if '.' in x1 and '.' in x2:
            print(f'Корни уравнения - {x1} , {x2}')
        else:
            print('Не вещественное число')
    elif D == 0:
        x1 = (-b + D) / 2 * a
        if '.' in x1:
            print(f'Корень уравения - {x1}')
        else:
            print('Не вещественное')
    else:
        print('Не имеет корней')
else:
    print('Старший коэффицент не может быть равна нулю')

birth_year = int(input("Введите год рождения: ")) #4.17
birth_month = int(input("Введите номер месяца рождения (1-12): "))
current_year = int(input("Введите текущий год: "))
current_month = int(input("Введите номер текущего месяца (1-12): "))
age = current_year - birth_year
if current_month < birth_month:
    age -= 1

print(f"Возраст человека: {age} полных лет")

S_kvadrat = float(input('Введитве площадь квадрата: ')) #4.18
S_kruq = float(input('Введите площадь круга: '))
if S_kvadrat // S_kruq > 0:
    print('Круг помещается в квадрат')
elif S_kruq // S_kvadrat > 0:
    print('Квадрат помещается внутрь круга')
else:
    print('Никакой никуда не помещается')

S_kruq = float(input('Введите площадь круга: ')) #4.19
S_treuqolnik = float(input('Введите площадь равностороннего треугольника: '))
if S_treuqolnik // S_kruq:
    print('Круг поместиться в треугольник')
elif S_kruq // S_treuqolnik:
    print('Треугольник поместиться в круг')
else:
    print('Никакой никуда не поместиться')

print("Введите координаты первого прямоугольника:") #4.20
x1_left = float(input("x левого нижнего угла: "))
y1_bottom = float(input("y левого нижнего угла: "))
x1_right = float(input("x правого верхнего угла: "))
y1_top = float(input("y правого верхнего угла: "))
print("\nВведите координаты второго прямоугольника:")
x2_left = float(input("x левого нижнего угла: "))
y2_bottom = float(input("y левого нижнего угла: "))
x2_right = float(input("x правого верхнего угла: "))
y2_top = float(input("y правого верхнего угла: "))
x_min = min(x1_left, x2_left)
y_min = min(y1_bottom, y2_bottom)
x_max = max(x1_right, x2_right)
y_max = max(y1_top, y2_top)
print("\nКоординаты минимального прямоугольника, содержащего оба:")
print(f"Левый нижний угол: ({x_min}, {y_min})")
print(f"Правый верхний угол: ({x_max}, {y_max})")

number1 = float(input('Введите вещесетвенное число: ')) #4.99 a)
number2 = float(input('Введите вещественное число: '))
if number1 > number2:
    print(f'Наибольшое - {number1}')
else:
    print(f'Наибольшое число - {number2}')

number1 = float(input('Введите вещесетвенное число: ')) #4.99 b)
number2 = float(input('Введите вещественное число: '))
max_number = number2
if number1 > number2:
    max_number = number1
    print(f'Наибольшое число- {max_number}')

print(f'Наибольшее число - {max_number}')

number1 = float(input('Введите вещесетвенное число: ')) #4.100 a)
number2 = float(input('Введите вещественное число: '))
if number1 > number2:
    print(f'Наибольшое число- {number1}')
    print(f'Наименьшее число - {number2}')
else:
    print(f'Наибольшое число - {number2}')
    print(f'Наименьшее число - {number1}')

number1 = float(input('Введите вещесетвенное число: ')) #4.100 b)
number2 = float(input('Введите вещественное число: '))
max_number = number1
min_number = number2
if number1 < number2:
    max_number = number2
    min_number = number1 
    print(f'Наибольшое число- {max_number} , наименьшее число - {min_number}')

print(f'Наибольшее число - {max_number} , наименьшее число - {min_number}')

number1 = float(input('Введите вещесетвенное число: ')) #4.101 a)
number2 = float(input('Введите вещественное число: '))
number3 = float(input('Введите вещественное число: '))
max_num = number1
if number2 > max_num:
    max_num = number2
if number3 > max_num:
    max_num = number3

print("Наибольшее число:", max_num)

number1 = float(input('Введите вещесетвенное число: ')) #4.101 b)
number2 = float(input('Введите вещественное число: '))
number3 = float(input('Введите вещественное число: '))
min_num = number1
if number2 < min_num:
    min_num = number2
if number3 < min_num:
    min_num = number3

print("Наименьшее число:", min_num)

number1 = float(input('Введите вещественное число: ')) #4.102 a)
number2 = float(input('Введите вещественное число: '))
number3 = float(input('Введите вещественное число: '))
number4 = float(input('Введите вещественное число: '))
max_number = number1
if number2 > max_number:
    max_number = number2
if number3 > max_number:
    max_number = number3
if number4 > max_number:
    max_number = number4

print(f'Наибольшое число - {max_number}')

number1 = float(input('Ввелите вещественное число: ')) #4.102 b)
number2 = float(input('Введите вещественное число: '))
number3 = float(input('Введите вещественное число: '))
number4 = float(input('Введите вещественное число: '))
min_number = number1
if number2 < min_number:
    min_number = number2
if number3 < min_number:
    min_number = number3
if number4 < min_number:
    min_number = number4

print(f'Наименьшее число - {min_number}')

x = float(input("Введите число: ")) #4.103

if x < 0:
    x = -x

print("Абсолютная величина числа:", x)

a = float(input("Введите первое число: ")) #4.104
b = float(input("Введите второе число: "))
if a < 0:
    a = -a
if b < 0:
    b = -b

half_sum = (a + b) / 2

print("Полусумма абсолютных величин =", half_sum)

number = float(input('Введите вещественное число: ')) #4.105
number2 = number / 2
number3 = float(input('Введите вещественное число: '))
if number3 < 0:
    number3 = - number3

if number2 > number3:
    print(f'Число - {number3}')

number = float(input('Введите число: ')) #4.106
number2 = float(input('Введите число: '))
if math.sqrt(number2) < number:
    number2 = number2 * 5
    print(f'Второе увеличенное число - {number2}')

number = int(input('Введите число: ')) #4.107
number1 = int(input('Введите число: '))
number2 = int(input('Введите число: '))

if number % 2 == 0:
    print(f'Первое число четное - {number}')
elif number1 % 2 == 0:
    print(f'Второе число четное - {number1}')
elif number2 % 2 == 0:
    print(f'Третье число четное - {number2}')
else:
    print('Нет ниодного четного числа')

number = float(input('Введите вещественное число: ')) #4.108
number1 = float(input('Введите вещественное число: '))
number2 = float(input('Введите вещественное число: '))

if number > 0:
    number = number**2
    print(f'Возведен в квадрат - {number}')
if number1 > 0:
    number1 = number1**2
    print(f'Возведен в квадрат - {number1}')
if number2 > 0:
    number2 = number2**2
    print(f'Возведен в квадрат - {number2}')
else:
    print('Все отрицательные')

number = float(input('Введите вещественное число: ')) #4.109
number1 = float(input('Введите вещественное число: '))
number2 = float(input('Введите вещественное число: '))

if 1.6 <= number <= 3.8:
    print(f'Значение попадает в промежуток - {number}')
if 1.6 <= number1 <= 3.8:
    print(f'Значение попадает в промежуток - {number1}')
if 1.6 <= number2 <= 3.8:
    print(f'Значение попадает в промежуток - {number2}')
else:
    print('Никакой не попадает в этот промежуток')