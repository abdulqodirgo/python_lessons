student_0 = {
            'name':"frank",
            'surname':"copperfield",
            'age':22,
            'major':"business management",
            'a_year':4
            }
#____________________________________________________________


# ().items
print(student_0.items()) #the result is confusing, therefore we use 'for' cycle together with ().items
for key, value in student_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

smartphones = {
                'steve jobs' : "iphone 14",
                'kim in ae' : "samsung s23",
                'chan kayshi' : "huawei p50",
                'jack ma' : "xiaomi note 14",
                'rasmussen' : "nokia 6233"
                }
for k,q in smartphones.items():
    print(f"\n{k.title()}`s smartphone model is \"{q}\"")
#____________________________________________________________

    
# ().keys
products = {
            'apple': 3.49, 
            'orange juice': 8.49, 
            'milk': 2.99,
            'fresh baked bread' : 3.99,
            'coffee': 2.99,
            'sour cream' : 1.99,
            'cereals' : 5.99
            }

print ("\n\nThe products that are consumed in breakfast:")
for prod in products.keys():
    print(prod.title())

basket = ['orange juice', 'milk', 'coffee','nuts', 'chocolate']
print("Need to buy products for the breakfast today are:", basket)
for prod in products:
    if prod in basket:
        print(f"{prod.title()} is available and costs {products[prod]} dollars")
for item in basket:
    if item not in products:
        print(f"I could not find {item.title()}, please show me where are they, thanks.")
#____________________________________________________________


# sorted()
print("\n\nProducts available in the store in alphabetical order:")
for prod in sorted(products):
    print(prod.title())    
#___________________________________________________________


#.values ()
print("\n\nUsers prefer to use following smartphonese:")
for mobile in smartphones.values():
    print(mobile)
#___________________________________________________________


#set()
phone_users = {
                'User1': "Nokia",
                'User2': "Nokia",
                'User3': "iPhone",
                'User4' : "xiaomi",
                'User5' : "Nokia",
                'User6' : "samsung",
                'User7' : "samsung",
                'User8' : "Huawei",
                'User9' : "iPhone",
                'User10' : "Blackberry"
                }
print("\n\nUsers prefer to use following smartphonese:")
for mobile in set(phone_users.values()):
    print(mobile)
print("\n\n")
#________________________________________________________

#class set
toys = {'ball', 'lamp', 'doll', 'car', 'ball', 'bear', 'car'}
print(toys)#set type selects each elements only once look that we had 2 balls, but in console there is only 1



#________________________________________________________
#AMALIYOT
dictionary = {
                'book': "kitob",
                'notebook': "daftar",
                'pencil': "qalam",
                'box': "korobka",
                'water':"suv",
                'soap': "sovun",
                'pen': "ruchka",
                'melon': "qovun",
                'apple': "olma",
                'wolf': "bo`ri"
                }
for x,y in sorted(dictionary.items()):
    print(f"\nENG {x}")
    print(f"UZB {y}")
    
countries ={
            'morocco' : "Rabat",
            'egypt': "Cairo",
            'palestine' : "Jerusalem",
            'qatar' : "Doha",
            'italy' : "Rome",
            'france' : "Paris",
            'england' : "London",
            'china' : "Beijing",
            'brazil' : "Brazilia",
            'australia' : "Canberra",
            'japan' : "Tokyo",
            'ukraine' : "Kiev",
            'poland' : "Warsaw"             
            }
print("\n\nCountries by alphabertical order:")
for country in sorted(countries.keys()):
    print(f"{country.upper()}")
    
print("\n\nCapitals by alphabetical order:")
for capital in sorted(countries.values()):
    print(f"{capital.title()}")

state = input("\n\nPlease write a country name, and we will tell its capital: >>> ").lower()
capital_c = countries.get(state)
if capital_c == None:
    print("Unfortunately, we do not have information about it in our system.")
else:
    print(f"The capital of {state.upper()} is {capital_c.title()}.")
    