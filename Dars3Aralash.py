# 1
# while True:
#     def profil(ism = '', yosh = None, t_raqami = None):
#         """Foydalanuvchi haqida malumot oluvchi funksiya """
#         pro ={
#             'Ism':ism,
#             'Yosh':yosh,
#             'T_raqam':t_raqami
#         }
#         return pro 
    
#     oz = 0
#     ism = input("Ismingizni kiriting; ")
#     yosh = input("Yoshingizni kiriting; ")
#     t_raqam = input("Telefon raqamingizni kiriting; ")

#     try:
#         yosh = int(yosh)
#         t_raqam = int(t_raqam)
#     except:
#         oz = 1

#     if oz == 1:
#         print("INt tipidagi malumot kiriting")
#         continue
#     # global Foydalanuvchi
#     Foydalanuvchi = (ism,yosh,t_raqam)
#     for i in Foydalanuvchi:
#         if i == "":
#             oz = 1
#     if oz == 1:
#         print("Ismingizni kiritmadingiz ")
#         continue
#     break
# if Foydalanuvchi[1] <= 18:
#     print("Kechirasiz siz dasturdan toliq foydalana olmaysiz ")
# else:
#     print("Siz uchun hamma imkoniyatlar ochiq ")

# 1.1

# jami = []
# def talaba_haqida(ism,yosh):
#     talaba = {
#         'Ism': ism,
#         'Yosh': yosh
#     }
#     jami.append(talaba)

# oz = 1
# while oz < 6:
#     ism = input(f'{oz}-Talabani ismini kiriting; ')
#     yosh = int(input(f"{ism.capitalize()}ning yoshini kiriting; "))
#     talaba_haqida(ism, yosh)
#     oz += 1

# jami.sort(key = lambda x:x['Yosh'])

# for i in jami:
#     print(f"{i['Ism']}ning yoshi {i["Yosh"]} da")

#2

# son = int(input("Nechta fibanachi soni chiqsin; "))
# oz = 0
# a1 = 0
# a2 = 1
# while oz < son:
#     a3 = a1 + a2
#     a1 = a2
#     a2 = a3
#     print(a1)
#     oz+=1

# 3

# pochta = input("Pochtangizni kiriting; ")

# if '@' in pochta:
#     if "@gmail.com" in pochta:
#         print("gmail")
#     elif "@yahoo.com" in pochta:
#         print("yahoo")
#     elif "@outlook.com"  in pochta:
#         print("outlook")
#     else:
#         print("Bunaqa email yo'q bizning bazamizda ")
# else:
#     print("Bunday xolatda email yozib bolmaydi ")

# 4
# jami = []
# soni = int(input("Nechi xil maxsulot olasiz "))
# for i in range(soni): 
#     maxsulot = input(f"{i+1}-maxsulot nomini kiriting; ")
#     narx = float(input(f"{maxsulot} narxini kiriting; "))
#     maxsulotlar = {
#         "Ismi":maxsulot,
#         "Narxi":narx
#     }
#     jami.append(maxsulotlar)
# narxJami = []
# for i in jami:
#     narxJami.append(i["Narxi"])
# if sum(narxJami) >= 100:
#     print(f"Sizning jami xaridingiz 100 mingdan oshgani uchun 10% lig chegirma bor ")
# else:
#     print("Dokonimizdan xarid qilganingiz uchun raxmat ")

# 5

# jami = []
# print("10 ta son kiriting")
# for i in range(1, 11):
#     son = int(input(f"{i}-soni kiriting; "))
#     jami.append(son)
# sonTupl = set()
# takroriSon = []
# for i in jami:
#     if i not in sonTupl:
#         sonTupl.add(i)
#     else:
#         takroriSon.append(i)
# print("Takrorlanmagan sonlar")
# for i in jami:
#     if i not in takroriSon:
#         print(i)

# 6

print("Talabalarni Baxolang minimal 70 maksimal 90 baxo qoying ")
son = int(input("Nechta talaba kiritasiz; "))
jami = []
for i in range(son):
    ism = input(f"{i+1}-talabani kiriting; ")
    baxo = int(input(f"{ism}ning baxosini kiriting; "))
    talabalar = {
        "Ism":ism,
        "Baxo":baxo
    }
    jami.append(talabalar)
for i in jami:
    if i["Baxo"] <= 70:
        print(f"{i["Ism"]}ning baxosi yomon")
    elif i["Baxo"] > 70 and i["Baxo"] <=80:
        print(f"{i["Ism"]}ning baxosi yaxshi")
    elif i["Baxo"] > 80 and i["Baxo"] <=90:
        print(f"{i["Ism"]}ning baxosi Alo")
    else:
        print("Bunday baxo yoq ")


