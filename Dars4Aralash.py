# 1 

# kod = 1234
# while True:
#     pin = int(input("Parolni kiriting; "))
#     if kod == pin:
#         break
#     else:
#         print("Xato kod terdingiz !!!! ")
# balans = 50000
# while True:
#     id = input("""
#     "Quyidagi bo'limlardan birini tanlang "
# 1)Balans ko'rish
# 2)Pul qo'shish
# 3)Pul yechish
# 4)chiqish
# >>> """)
#     if id == "1":
#         print("Sizning balansingizda", balans, "pul bor ")
#     elif id == "2":
#         qosh = int(input("Qancha pul qo'shmoqchisz; "))
#         balans += qosh
#     elif id == "3":
#         ayeish = int(input("Qancha pul yechmoqchisiz; "))
#         if balans < ayeish:
#             print("Kechirasiz xisobingizda pul yetarli emas !!!! ")
#         else:
#             balans -= ayeish
#     elif id == "4":
#         break
#     else:
#         print("Xato bolim tanladingiz ")

# 2 

maxsulotlar = {
    'olma':{
        'narx':15000
    },
    'banan':{
        'narx':25000
    },
    'ananas':{
        "narx":45000
    },
    'apelsin':{
        'narx':50000
    },
    'mandarin':{
        'narx':25000
    }
}
jami = 0
for i in range(5):
    olmoqchi = input(f"{i+1}- Maxsulotingiz nomini kiriting; ")
    if olmoqchi in maxsulotlar:
        soni = float(input("Necha kilo olmoqchisiz; "))
        yig = soni * maxsulotlar[olmoqchi]['narx']
        jami += yig
    else:
        print("Kechirasiz siz qidirgan maxsulot bizning do'konimizdan topilmadi !!! ")
print("Jami sizning xaridingiz", jami)
if jami > 150000:
    print("Sizga 10% chegirmamiz bor ")
elif jami == 0:
    print("Keyingi kelishingizga sizning xam maxsulotlaringizni olib kelamiz ")
    

