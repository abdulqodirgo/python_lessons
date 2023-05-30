car_0 = {
        'model': "camry",
        'color': "black",
        'year': 2020,
        'price': 32000,
        'mileage': 50000,
        'transmission': "auto"
        }

car_1 = {
        'model': "genesis",
        'color': "silver",
        'year': 2023,
        'price': 49000,
        'mileage': 3000,
        'transmission': "auto"
        }

car_2 = {
        'model': "camaro",
        'color': "red",
        'year': 2019,
        'price': 25000,
        'mileage': 50000,
        'transmission': "manual"
        }

#Nesting - is the process putting several dictionaries into one list or similar

cars = [car_0, car_1, car_2]
for car in cars:
    print(f"\n\nModel: {car['model'].title()}, ")
    print(f"Color: {car['color']}, ")
    print(f"Year: {car['year']}, the price: ${car['price']}.")
    
print(f"\n\n{cars[2]['color'].title()} "
      f"{cars[2]['model']}\n\n")

#sample
toyotas = []
for n in range(10):
    new_car = {
        'make': "toyota",
        'model': "land cruiser",
        'color': None,
        'year': 2023,
        'price': None,
        'mileage': 0,
        'transmission' : "auto"
                }
    toyotas.append(new_car)
for toyota in toyotas[:3]:
    toyota['color']="black"

for toyota in toyotas[3:6]:
    toyota['model']="highlander"
    toyota['color']="white"

for toyota in toyotas[6:8]:
    toyota['color']="silver"
    toyota['transmission'] = "auto"
    toyota['model'] = "camry"
    
for toyota in toyotas[8:]:
    toyota['color']="silver"
    toyota['transmission'] = "mechanic"
    toyota['model'] = "camry"
    
for toyota in toyotas:
    if toyota['model'] == "land cruiser":
        toyota['price'] = 120000
    if toyota['model'] == "highlander":
        toyota['price'] = 70000
    if toyota['model'] == "camry":
        toyota['price'] = 40000
    if toyota['transmission'] == "mechanic":
        toyota['price'] = 35000

print (toyotas)        
#print(f"Make: {toyota['make'].upper()}\n"
#      f"Model: {toyota['model'].title()}\n"
#      f"Color: {toyota['color']}\n"
#      f"Year: {toyota['year']}\n"
#      f"Price: {toyota['price']}\n"
#      f"Mileage: {toyota['mileage']}\n"
#      f"Transmission: {toyota['transmission']}")


#____________________________________________________

#SAMPLE for inserting lists into values of the dictionary:
coders = {
        'john': ['python', 'c++'],
        'mark': ['html', 'css', 'js'],
        'glen': ['php','sql'],
        'mary': ['python', 'php'],
        'steve': ['c++', 'c#']
        }
for name, languages in coders.items():
    print(f"\n{name.title()} can work on following programming languages: ")
    for language in languages:
        print(f" {language.upper()}", end="")
        
        
#______________________________________________________        
        

#SAMPLE for inserting dictionary for values of the dictionary:
collegues ={
            'jim': {
                    'position': "OPS Manager", 
                    'experience': 5,
                    'languages': ["pyhton","js","html"]
                    },
            
            'jeff': {
                    'position': "CRM Manager",
                    'experience': 3,
                    'languages': ['c++', 'c#', 'js']
                    },
            
            'frank': {
                    'position': "Engineer",
                    'experience': 5,
                    'languages': ['python', 'swift', 'golang']
                    }
            
            }
for name, info in collegues.items():
    print(f"\n\n {name.title()} works as a {info['position']}."
          f"He has been working for {info['experience']} years."
          f"Here are the programming skills he owns in terms of coding: {info['languages']}.")
#____________________________________________________________________
#AMALIYOT
celeb_0 ={
            'name': "messi",
            'b_year': 1988,
            'club': "psg",
            'country': "Argentina"
            } 

celeb_1 = {
            'name': "ronaldo",
            'b_year': 1985,
            'club': "al-nasr",
            'country': "Portugal"
            }
celeb_2 = {
            'name': "benzema",
            'b_year': 1987,
            'club': "real madrid",
            'country': "France"
            }
celebs = [celeb_0, celeb_1, celeb_2]
for celeb in celebs:
    print(f"{celeb['name'].title()} was born in {celeb['b_year']}, he is from {celeb['country']} and plays for {celeb['club'].upper()}")















