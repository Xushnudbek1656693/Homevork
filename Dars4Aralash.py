balans = 50000
while True:
    id = input("""
    "Quyidagi bo'limlardan birini tanlang "
1)Balans ko'rish
2)Pul qo'shish
3)Pul yechish
4)chiqish
>>> """)
    if id == "1":
        print("Sizning balansingizda", balans, "pul bor ")
    elif id == "2":
        qosh = int(input("Qancha pul qo'shmoqchisz; "))
        balans += qosh
    elif id == "3":
        ayeish = int(input("Qancha pul yechmoqchisiz; "))
        if balans < ayeish:
            print("Kechirasiz xisobingizda pul yetarli emas !!!! ")
        else:
            balans -= ayeish
    elif id == "4":
        break
    else:
        print("Xato bolim tanladingiz ")