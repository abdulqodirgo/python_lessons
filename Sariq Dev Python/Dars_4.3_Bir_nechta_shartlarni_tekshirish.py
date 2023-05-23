
# ELIF - ELSE

#yosh = int(input("Enter the AGE: -> "))
#if yosh <= 7:
#    price = 0
#    print("Free")
#elif yosh <= 12:
#    price = 5
#    print("Price =  $5")
#elif yosh <= 18:
#    price = 10
#    print("Price = $10")
#elif yosh >= 65:
#    price = 7
#    print("Price =  $7")
#else:
#       price = 30
#        print("Price = $30")
#--------------------------------------------------

# AND va OR 

#kun = input("Bugun nima kun? >>> ")
#if kun == "shanba" or kun == "yakshanba":
#    print("Bugun dam olish kuni")
#else:
#    print("bugun ish kuni")

#kun = input("Bugun nima kun? >>> ")
#harorat = float(input("Havo harorati qanday? >>> "))
#if kun == "yakshanba" and harorat>=30:
#    print("Chomilgani boramiz!")
#elif kun == "yakshanba" and harorat <30:
#    print("Uyda dam olamiz!")
#--------------------------------------------------

# AND OR ELIF

#kun = input("Bugun nima kun? >>> ")
#harorat = float(input("Gradus qanaqa? >>> "))
#if kun == "shanba" or kun == "yakshanba" and harorat >= 30:
#    print("Bugun dam olish kuni va issiq bulgani uchun cho`milgani boramiz!")
#elif kun == "shanba" or kun == "yakshanba" and harorat < 30:
#    print("Bugun dam olish kuni bulishiga qaramasdan kucha sovuq bulganiga, uyda dam olamiz")
#--------------------------------------------------

#BOOLEAN 

#narx = 35000
#choy = True #boolean process
#salat = False #boolean process
#if choy and salat:
#    narx = narx + 20000
#elif choy or salat:
#    narx = narx + 10000
#print(f"Jami narx {narx} so`m buldi")
#___________________________________________________

#narx = 25000
#non = 1 # = 1 yokida = True
#choy = 1 
#sok = 0 # = 0 yokida = False bular BOOLEAN ga misollar
#salat = 1
#desert = 0
#print(f"Lag`mon narxi = {narx}")
#if non:
#    print("Non olindi: 5000")
#    narx = narx + 5000
#if choy:
#    print("Choy olindi: 3000")
#    narx = narx + 3000
#if sok:
#    print("Sok olindi: 10000")
#    narx = narx + 10000
#if salat:
#    print ("Salat olindi: 8000")
#    narx = narx + 8000
#if desert:
#    print("Desert olindi: 15000")
#   narx = narx + 15000
#print(f"Jami taomlanish xarajati {narx}ga teng.")

#-------------------------------------------------
# IN - NOT IN operatorlar
#menu = ['osh', 'somsa', 'lagmon', 'shashlik', 'norin']
#ovqat = input("Nima ovqat yeyishni hohlaysiz? >>> ")
#if ovqat in menu:
#    print("Buyurtma qabul qilindi")
#else: print("Suragan ovqatingiz menuda yo`q")

menu = ['osh', 'somsa', 'lagmon', 'shashlik', 'norin']
zakaz = ['somsa','mastava', 'salat', 'norin']
print(f"Buyurtma qilingan ovqatlar: {zakaz}")
for ovqat in zakaz:
    if ovqat in menu:
        print(f"Menuda {ovqat} bor")
    else:
        print(f"Kechirasiz menuda {ovqat} yo`q.")

































































