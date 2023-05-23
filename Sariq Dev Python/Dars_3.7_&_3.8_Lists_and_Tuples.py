cars = ['bmw', 'mercedes', 'audi', 'porsche','volkswagen','opel']
cars.sort()
print("German car brands:\n>>> ", cars)
cars.sort(reverse=True)
print("Reverse sorted car brands:\n>>>",cars)
sorted(cars)
print(sorted(cars))
print(cars)


ages = [28,25,53,51,19,21,1,1]
print("\n\nMy family member`s age are as following: >>> ", ages)
print("\nAge Lowest first: >>> ", sorted(ages))
print("\nAge Oldest first: >>> ", sorted(ages, reverse= True))

# Having sortified we are inputting the data to variable section 
ages.sort()

viloyatlar =['Andijon','Namangan','Fargona','Toshkent','Sirdaryo','Jizzax','Samarqand']
print("\nUzbekiston viloyatlar ruyhati East to West: >>> ",viloyatlar)

viloyatlar.reverse()
print("\nUzbekiston viloyatlar ruyhati West to East: >>>", viloyatlar)

viloyatlar.sort()
print("\nTotal number of viloyatlar: >>> ",len(viloyatlar),"\nViloyatlar alphabetically sorted: >>>", viloyatlar,"\n")

#range funksiyasi
sonlar = list(range(-3,8))
print("-3 dan 8 gacha bulgan sonlar ruyhati: >>> ",sonlar,"\n\n")

#range ichida qadam belgilash yokida selective raqam tanlash
toq_sonlar = list(range(-3,8,2)) # 2 -bu 2 qadam oralatib tanlashlik degani))
print("-3 dan 8 gacha sonlar ichidagi toq sonlar: >>>",toq_sonlar,"\n\n")

# Min va Max qiymatlar
narxlar = [350, 800, 1200, 1700, 2200, 3000, 3500]
print(narxlar,"\nMinimum rate: >>> ",min(narxlar),"\nMaximum rate: >>> ",max(narxlar),"\nSummary: >>> ",sum(narxlar))


# nusxa olish [:] funkciya
cars = ['Bentley', 'Mercedes', 'Rollce Royce', 'Porsche','BMW','Volkswagen']
my_cars = cars[:] 

#.append
my_cars.append("Ferrari")
print(my_cars)

#.remove
my_cars.remove('BMW')
print(my_cars)

# del
del my_cars[1]
print(my_cars)

#ranged elements from the list
print(my_cars[1:3])

print(cars, "\n", my_cars, "Units of my cars: >>> ",len(my_cars),"\n\n\n")


#Tuples
toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
print("Type of the list above is >>>",type(toys), "we can`t make changes on it.\n")
print("In order to make changes we must change the type of toys from tuple to regular list, once we have the 'LIST' type we can make changes: ")
toys = list(toys)
print(type(toys)) #change has been made, now we can edit the list
toys.append('lego') #added element
toys.remove('dino') #removed the element
print(toys) # updated list
print(toys[0:2]) # requested to print selected range elements
print("Right now our updated <toys list> is in 'list' type and it is changable.\n",
      "If we want to return back to 'tuple' type we do as following:\n >>> toys = tuple(toys)")
toys = tuple(toys)
print("This is the final list after adjustments: >>> ",toys) 
print(type(toys)) #we see it back to TUPLE again


#AMALIYOT

#1
davlatlar = ['Japan', 'China', 'Malaysia', 'Italy','Germany','France','Sweden']
print("\n\nList of countries: >>> ",davlatlar,"\nNumbers: >>>",len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar,reverse= True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.reverse()
print(davlatlar,"n")

#2
juft_raqamlar = list(range(120,1200,2))
print(juft_raqamlar,"\nPaired numbers from 120 to 1200")
print("Summary of all numbers = ",sum(juft_raqamlar))
print("Max Number - Min number = 1198 - 120 = ",max(juft_raqamlar)-min(juft_raqamlar))
print("Quantity of numbers: >>> ",len(juft_raqamlar))
print("First 10 numbers: >>> ",juft_raqamlar[0:10],"\nMiddle 10 numbers: >>> ",juft_raqamlar [265:275],"\nLast 10 numbers: >>> ", juft_raqamlar [530:540])

#3
taomlar = ['Palov', 'Lagmon', 'Somsa', 'Shashlik', 'Mastava']
nonushta = taomlar[:]
nonushta.remove('Palov')
del nonushta[0]
print(nonushta)
nonushta.append("Tvorog")
nonushta.insert(0,"Buxanka")
print("Nonushta: ",nonushta)
print("Taomlar: ",taomlar)
nonushta = tuple(nonushta)
print(type(nonushta))
taomlar[0]="Osh"
print(taomlar)
nonushta =list(nonushta)
nonushta[0]="Non va Qaymoq"
print(nonushta)











































