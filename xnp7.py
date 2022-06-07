from  random import randint

counts = 1
money = 1000
money -= 10
a = randint(1,6) + randint(1,6)
print(a)
if a == 7 or a == 11:
    money += 20
    print(f"经过{counts}轮，The player win!现在有{money}元。")
elif a == 2 or a == 3 or a == 12:
    print(f"经过{counts}轮，The banker win!现在有{money}元。")
else:
    while money > 0 :
        money -= 10
        counts += 1
        b = a
        a = randint(1,6) + randint(1,6)
        print(a)
        if a == 7:
            print(f"经过{counts}轮，The banker win!现在有{money}元。")
            break
        elif a == b:
            money += 20
            print(f"经过{counts}轮，The player win!现在有{money}元。")
            break

def add(a=1, b=2, c=3):
    """三个数相加"""
    return a + b + c