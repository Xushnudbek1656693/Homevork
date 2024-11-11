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

jami = []

def talaba_haqida(ism,yosh):
    talaba = {
        'Ism': ism,
        'Yosh': yosh
    }
    jami.append(talaba)

oz = 1
while oz < 6:
    ism = input(f'{oz}-Talabani ismini kiriting; ')
    yosh = int(input(f"{ism.capitalize()}ning yoshini kiriting; "))
    talaba_haqida(ism, yosh)
    oz += 1

jami.sort(key = lambda x:x['Yosh'])

for i in jami:
    print(f"{i['Ism']}ning yoshi {i["Yosh"]} da")