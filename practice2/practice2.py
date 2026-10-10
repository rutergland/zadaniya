# 1
ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
en = "abcdefghijklmnopqrstuvwxyz"


def to_cesar(s, num):
    res = ""
    for c in s:
        ch = c.lower()
        if ch in en:
            c_num = en.index(ch)
            ind = c_num + num
            if c.isupper():
                res += en[ind % 26].upper
            else:
                res += en[ind % 26]
        elif ch in ru:
            c_num = ru.index(ch)
            ind = c_num + num
            if c.isupper():
                res += ru[ind % 26].upper
            else:
                res += ru[ind % 26]
        else:
            res += c
    return res


def from_cesar(s, num):
    return to_cesar(s, -num)


# a = "abamaлох"
# b = to_cesar(a, 3)
# c = from_cesar(b, 3)
# print(b)
# print(c)


# 2
def check_winners(scores, student_score):
    best = []
    sc = scores
    a = 0
    while a < 3:
        a += 1
        b = sc.index(max(sc))
        best.append(sc.pop(b))
    if student_score in best:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей!")


scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
student_score = 52
# check_winners(scores, student_score)


# 3
def print_pack_report(num):
    p = False
    t = False
    for n in range(num, 0, -1):
        p = n % 5 == 0
        t = n % 3 == 0
        if p and t:
            print(f"{n} - расфасуем по 3 или по 5")
        elif p and not (t):
            print(f"{n} - расфасуем по 5")
        elif not (p) and t:
            print(f"{n} - расфасуем по 3")
        else:
            print(f"{n} - не заказываем!")


# print_pack_report(14)


# 4
import random as rand


def password():
    sym = "abcdefghijklmnopqrstuvwxyz"
    ch = "!@#$%^&*()_+=-"
    nums = "0123456789"

    l = int(input("Введите длину пароля: "))
    verh = input("Заглавные буквы? (д/н): ").lower() == "д"
    nizh = input("Строчные буквы? (д/н): ").lower() == "д"
    spec = input("Спецсимволы? (д/н): ").lower() == "д"
    num = input("Цифры? (д/н): ").lower() == "д"

    v = []
    p = []

    if verh:
        v.append(sym.upper())
        p.append(rand.choice(sym.upper()))
    if nizh:
        v.append(sym)
        p.append(rand.choice(sym))
    if spec:
        v.append(ch)
        p.append(rand.choice(ch))
    if num:
        v.append(nums)
        p.append(rand.choice(nums))
    if v == []:
        print("Нужно выбрать хотя бы один тип символов")
        return
    if l < len(v):
        print(f"Длина должна быть не меньше {len(v)}")
        return

    all = "".join(v)
    while l > len(p):
        p.append(rand.choice(all))

    rand.shuffle(p)
    res = "".join(p)
    print(f"Сгенерированный пароль длиной {l}: {res}")


# password()


# 5
to_roman_s = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}


def to_roman(nums):
    romans = []
    for num in nums:
        roman = ""
        s_near = "I"
        near = 1
        while num != 0:
            for s in to_roman_s:
                if num >= to_roman_s[s]:
                    near = to_roman_s[s]
                    s_near = s
            num -= near
            roman += s_near
        romans.append(roman)
    return romans


from_roman_s = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def from_roman(romans):
    nums = []
    for roman in romans:
        prev_val = 0
        num = 0
        for c in reversed(roman):
            val = from_roman_s[c]
            if val < prev_val:
                num -= val
            else:
                num += val
            prev_val = val
        nums.append(num)
    return nums


# roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]
# a = from_roman(roman_tests)
# b = to_roman(a)
# print(a)
# print(b)


# 6
level = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]


def viselica():
    s = input("Загадайте слово: ")
    wrong = 0
    guess = ["_"] * len(s)
    while wrong < 6 and "".join(guess) != s:
        print(level[wrong])
        print(guess)
        g = input("Введите букву: ")
        if g in s:
            for i, ch in enumerate(s):
                if ch == g:
                    guess[i] = g
            print("Вы угадали букву!")
        else:
            wrong += 1
            print("Вы не угадали букву!")
        print(level[wrong])
        print(guess)
    if "".join(guess) == s:
        print("Вы победили!")
    elif wrong == 6:
        print("Вы проиграли!")
    return


# viselica()
