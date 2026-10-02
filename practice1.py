import random
from collections import Counter

def celcium_perevod(temp_celcium):
    print(f'Цельсии: {temp_celcium}')
    temp_fr = temp_celcium * 1.8 + 32
    temp_kelv = temp_celcium + 273.15
    print('Фаренгейты:', temp_fr)
    print('Кельвины:', temp_kelv)

def opr(n):
    print(f'Число {n}:')
    if (n % 2 == 0):
        print('Чётное')
    else:
        print('Нечётное')
    if (n > 0):
        print('Положительное')
    elif (n < 0):
        print('Отрицательное')
    else:
        print('Ноль')
    if (10 <= n <= 50):
        print('Принадлежит диапозону [10, 50]')
    else:
        print('Не принадлежит диапозону [10, 50]')

def pass_gen():
    let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    special = "!@#$%^&*"
    pswrd = []
    for i in range(3):
        pswrd.append(random.choice(let))
    for i in range(3):
        pswrd.append(random.choice(num))
    for i in range(2):
        pswrd.append(random.choice(special))
    random.shuffle(pswrd)
    print ("".join(pswrd))

def char_use():
    text = input().lower()

    c = Counter(text)

    for s, count in c.items():
        print(f"Символ: {s} - {count} раз")

def simple_number(n):
    num = []
    for i in range(2, n+1):
        num.append(i)
    
    simple = []
    while len(num) > 0:
        s = num[0]
        simple.append(s)
        left = []
        for i in num:
            if i % s != 0:
                left.append(i)
        num = left
    print(simple)

def nat_num():
    n = int(input())
    razryad = 1
    mn = 1

    while n > 9 * mn * razryad:
        n -= 9 * mn * razryad
        razryad += 1
        mn *= 10

    for i in range(1 * mn, 10 * mn):
        if n <= razryad:
            print(str(i)[n - 1])
            break
        n -= razryad

nat_num()
    
#1
celcium_perevod(30)
#2
opr(30)
#3
pass_gen()
#4
char_use()
#5
simple_number(30)
#6
nat_num()
