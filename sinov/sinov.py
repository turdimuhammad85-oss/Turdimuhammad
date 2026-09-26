# import json
#
# a = 15
# b = False
# c = [1,2,3]
# d = {
#     "ism":"jasur",
#     "yosh":12
# }
# a_j = json.dumps(a)
# print(a_j)
# print(type(a_j))
# d_j = json.dumps(d, indent=4)
# print(d_j)
# print(type(d_j))
# import json
#
# a = "false"
# b = "{1:1}"
# print(type(1))
# print(2)
# a2 = json.loads(a)
# print(type(a2))
# print(a2)
# import json
# info = {
# import json
# info = {
# "ism":"Turdimuhammad",
#     "yili":"2011",
#     "Tugilgan joyi":"fargona viloyati buvayda tumani"
# }
# with open("info.json","w") as f:
#     json.dump(info,f)
# with open("info.json", "r") as f:
#     m = json.load(f)
#     print(m)
#     print(type(m))
# import time
# while True:
#     print("Sariq")
#     time.sleep(1)
#     print("Yashil")
#     print("Sariq")
#     time.sleep(1)
#     print("Yashil")
#     time.sleep(5)
#     print("Sariq")
#     time.sleep(1)
#     print("Qizil")
#     time.sleep(5)
#     print("Sariq")
#     time.sleep(1)
#     print("Yashil")
#     time.sleep(5)
#     print("Sariq")
#     time.sleep(1)
#     print("Qizil")
#     time.sleep(5)
# import datetime
# sana = datetime.date.today()
# print(sana)
# print(sana.year)
# print(sana.month)
# print(sana.day)
# print(f"men {sana.year} yil: {sana.month} oy: {sana.day} kunda tug'ulganman...")
# import datetime
# vaqt = datetime.time(23, 59, 59, 999999)
# print(vaqt)
#
# impor datetime
#
# hozir = datetime.datetime.now().strftime("%H:%M:%S")
# print(hozir)
# time.sleep(1)
# import datetime
# hozir = datetime.datetime.now()
# otmish = datetime.datetime(2027,5, 25)-hozir
# print(otmish)
# import datetime
# import time
#
# while True:
#     soat = int(input("soat: "))
#     minut = int(input("minut: "))
#     sekund = int(input("sekund: "))
#
#     muddat = datetime.datetime.now() + datetime.timedelta(hours=soat,minutes=minut,seconds=sekund)
#
#     while datetime.datetime.now() < muddat:
#         qolgan = muddat - datetime.datetime.now()
#         soat = qolgan.seconds // 3600
#         minut = (qolgan.seconds % 3600) // 60
#         sekund = qolgan.seconds % 60
#         print(f"{soat:02}:{minut:02}:{sekund:02}")
#         time.sleep(1)
#     print("\nBomba portlatildi!")
#     break
# class User():
#     def __init__(self, name):
#         self.name = name
# user1 = User("Jasur")
# user2 = User("Qosim")
# user3 = User("Bobur")
# class Student():
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return self.name
# student1 = Student("Jasur")
# student2 = Student("Qosim")
# student3 = Student("Bobur")
# print(student1)
# class Maktab():
#     def __init__(self, nom, direktor, manzil, oquvchilar_soni):
#         self.nom = nom
#         self.direktor = direktor
#         self.manzil = manzil
#         self.oquvchilar_soni = oquvchilar_soni
# maktab1 = Maktab("1-maktab", "Shuhrat ergashev", "Buvayda tumani", 1000)
# n = f"1-maktab:\n"
# n += f"nom:{maktab1.nom}\n"
# n += f"direktor: {maktab1.direktor}\n"
# n += f"manzil: {maktab1.manzil}\n"
# n += f"o'quvchilar soni: {maktab1.oquvchilar_soni}\n"
# print(n)
# class User:
#     def __init__(self, first_name, last_name, email, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.__age = age
#     def __str__(self):
#      return f"{self.first_name} {self.last_name}"
#     def add_age(self):
#         self.__age += 1
#     def update_age(self, age):
#      if age <= 0:
#       print("yoshingizdan ayirib bo'lmaydi!")
#      else:
#         self.__age += age
#     def get_age(self):
#      return self.__age
#     def get_frist_name(self):
#         return self.first_name
# user1 = User("Turdimuhammad", "Abdulatifov", "123tm", 13)
# user2 = User("Bobur", "Qosimov", "123@gmail.com", 21)
# user2.update_age(1)
# print(user1.get_age())
# print(user2.get_age())
# class Olma():
#     """
#     mening olmam
#     dunyodagi eng
#     shirin olma
#     """
#     def __init__(self, dunyodagi, shirin):
#         self.dunyodagi = dunyodagi
#         self.shirin = shirin
# olmam = Olma("olmam", "shirin")
# print(olmam.dunyodagi)
# print(olmam.shirin)
# print(print.__doc__)
# print(Olma.__init__.__doc__)
# class Olma:
#     def __init__(self, nomi, turi, narxi, kilogram):
#         self.nomi = nomi
#         self.turi = turi
#         self.narxi = narxi
#         self.__kilogram = kilogram
#
#     def add_kilogram(self):
#         self.__kilogram += 1
#
#     def update_kilogram(self, kilogram):
#         if kilogram <= 0:
#             print("Kilogrammni kamaytirib bo'lmaydi!")
#         else:
#             self.__kilogram += kilogram
#
#     def get_kilogram(self):
#         return self.__kilogram
#
#
# olma = Olma("Tilla olma", "tilla", 70000000, 5)
#
# olma.update_kilogram(2)
#
# print("Nomi:", olma.nomi)
# print("Turi:", olma.turi)
# print("Narxi:", olma.narxi)
# print("Kilogram:", olma.get_kilogram())
# class Robot():
#     __robotlar_soni = 1
#     __robotlar_royxati = []
#
#     @classmethod
#     def get_robotlar(cls):
#         n = f"Robotlar soni: {cls.__robotlar_soni}\n"
#         n += f"Royxati: {cls.__robotlar_royxati}\n"
#         return n
#
#     def __init__(self, nom, narh, rang):
#         self.nom = nom
#         self.narh = narh
#         self.rang = rang
#
#         Robot.__robotlar_soni = 2
#         Robot.__robotlar_royxati.append(self.nom)
#
#         if self.rang == "oq":
#             print(self.nom)
#         else:
#             print(self.nom)
#
#
# robot1 = Robot("Uy roboti", 5000, "oq")
# robot2 = Robot("Tozalovchi robot", 3000, "qora")
# #
# # print(Robot.get_robotlar())










































































































































































































































































































































