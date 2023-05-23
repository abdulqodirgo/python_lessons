mevalar = ["olma", "anjir", "shaftoli","o`rik"] # matnli ruyhat
narxlar = [12000, 18000, 10900, 22000] #raqamli ruyhat
sonlar = ['bir','ikki', 3, 4, 5] # aralash ruyhat
ismlar = [] # bo`sh ruyhat


print("Birinchi meva: >>> ", mevalar[0])
print("Uchinchi meva: >>> ", mevalar[2])
print("Oxirgi meva: >>> ", mevalar[-1],"\n") # eng oxirgi elementni -1 qilib chaqirsak ham buladi


#.append() buyrugi bu listni oxiriga qushimcha qilishlik
mevalar.append("gilos")
mevalar[3]="nok" #[3]raqamli meva o`rik urniga nok quydik
mevalar[1]="mandarin"
print("Yangilangan mevalar ruyhati: \n>>>", mevalar)

# bo`sh ruyhat yaratib uni .append funksiyasi bilan tuldirib borishlik amaliyotda ruy berib turadi
cars=[]
cars.append('toyota')
cars.append('lexus')
cars.append('mazda')
print("\nMashinalar ruyhati:\n>>> ",cars)

#.insert bu ruyhat boshiga element tartib raqami va nomini qushishlik
cars.insert(0,"Bentley" )
print(cars)
cars.insert(1, "Rollce Royce")
print (cars)

# Elementni uchirish. Ikki xil buladi 1) Tartib raqami buyicha 2) Element Nomi buyicha
hayvonlar =['Mushuk', 'It', 'Sigir', 'Qo`chqor', 'Chayon']
print("\n\nUy hayvonlari, ammo ichida bitta ortiqchasi bor:\n>>> ",hayvonlar)

# 1) tartib raqami buyicha elementni uchirishlik >>> del list[element`s number]
del hayvonlar[-1]
print("Yangilangan hayvonlar ruyhati:\n>>> ", hayvonlar)


# 2) Element nomi bilan elementni uchirish >>> list.remove"name"
hayvonlar.remove("It")
print(hayvonlar)

# Element nomi bilan uchirilgandagi nyuanslar
mevalar= ['olma', 'mandarin', 'shaftoli','mandarin', 'nok', 'gilos']
print("\n\nMEVA ruyhatlari ustida ishlaymiz\n >>>", mevalar)
#bizda hozir 2ta mandarin bor, remove mandarin deymiz lekin faqat birinchisini uchiradi holos
mevalar.remove("mandarin")
print("Chapdan birinchi mandarin uchirildi va endi faqat bir dona qoldi:\n", mevalar)


# .pop elementni sugurib olish

bozorlik = ['Un', 'Yog`', 'Makaron', 'Go`sht', 'Guruch', 'Nutrilak', 'Pampers']
print("\n\nBozorliklar dastlabki ruyhati: >>> ", bozorlik)
mahsulot = bozorlik.pop(0),bozorlik.pop(-1)
print("\nMen", mahsulot, "sotib oldim")
print("Olinishi kerak bulgan qolgan mahsulotlar >>> ", bozorlik,"\n\n")


#AMALIYOT
ismlar = ['Sadulloh','Ibrohim', 'Asror']
print ("Salom", ismlar[0],"ishlaringiz yaxshimi?\n",
       ismlar[1], "Toshkent tinchmi?\n",
       ismlar[2], "Bro Canadadan qachon kelasiz?\n")

sonlar = [8,-4, 6, 2.2]
print( sonlar [0] + sonlar [2],"\n",
      sonlar[1] * sonlar[3],"\n",
      sonlar[2] / sonlar[3],"\n",
      sonlar[0] - sonlar[1]
      )

t_shaxslar = ['Umar r.a.','Xolid bin Valid', 'Sulton Abdulhamidxon']
z_shaxslar = ['Xasan qoriaka','Xusan qoriaka','Abdullo domla']
print("Men tarixiy shaxslardan", t_shaxslar.pop(0),"bilan kurishishni hohlardim."
      "\nZamonaviy shaxslardan esa", z_shaxslar.pop(0),"suhbatlaridan bahramand bulishni istayman.\n\n")

friends =[]
friends.append("Lampard")
friends.append("Gerrard")
friends.append("Pirlo")
friends.append("Messi")
friends.append("Iniesta")
friends.append("Mbappe")
friends.insert(0, "Ronaldo CR7")
print("Here is the list of best players which came into my mind:\n >>> ",friends,"\n")
friends.remove("Gerrard"), friends.remove("Lampard"),friends.remove("Pirlo")
print("Yet, some of them are not playing football anymore. Here is the list of currently playing ones: >>> ",friends)
friends.append("Benzema")
friends.insert(0, "Kevin De Bruyne")
friends.insert(3, "Pogba")
print("\nI forgot about some other players and just added them to the list, Here is the updated list:\n>>>",friends)






















































