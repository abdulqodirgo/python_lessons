#Dictionary
#_________________________________________________

car_0 = {'make':'toyota','model':'highlander','colour':'black'}
print(car_0['make'])
print(car_0['model'])
print(car_0,"\n\n")

#________________________________________________

#adding extra keys and value pairs to the dictionary
student_0 = {
    'name':'john hopkins',
    'age':28,
    'b_year': 1995,
    'body_fit': 'athletic'
    }
print(f"{student_0['name'].title()},\
      is a student and was born in {student_0['b_year']}, \
      he is {student_0['age']} year old.")
student_0['location'] = "Chicago IL"
student_0['major'] = "Computer Science"
print(student_0,"\n\n")
#________________________________________________

#Creating empty dictionary
student_1 = {}
student_1['name'] = "adam smith"
student_1['major'] = "Economics"
student_1['age'] = 25
print(f"Student name is {student_1['name'].title()}, he studies {student_1['major']} and he is {student_1['age']} year old")
del student_1['age']
print(student_1)
student_1['gender'] = 'Male'
print(student_1,"\n\n")

#__________________________________________________

#Method--> get() 
eng_uzb = {
            'apple':"olma",
            'peach':"nok",
            'melon':"qovun",
            'orange': "apelsin",
            'mulberry':"tut"
            }
print("Here is the English - Uzbek fruit dictioanry: \n",eng_uzb)
meva = eng_uzb.get('carrot',"There is no such fruit.")
print(meva, "\n\n")

#___________________________________________________

#AMALIYOT
#____________________________________________________
#1
brother = {'name' : 'aaron',
           'b_year': 2004,
           'age' : 19,
           'l_place': "UZB"
           }

print(f"Brother`s name is {brother['name'].title()},\
      He was born in {brother['b_year']}\
          he is living in {brother['l_place']}\
              he is currently {brother['age']} years old.\n\n")
#____________________________________________________

#2
family = {
            'father':"steak",
            'mother':"palov",
            'brother_1':"noodles",
            'brother_2':"somsa",
            'sister':"soup"
            }
print("This is the list of family member`s favorite food: \n",family,"\nNow will print only 3 meals that are mostly consumed: >>> ")
print(family['father'], family['brother_2'], family['sister'],"\n\n")

#____________________________________________________

#3
terms = {
        'print': "consolega chiqarish",
        'if': "agar",
        'else': "unday bolsa",
        'float':"o`nlik son",
        'int':"butun son",
        'del': "delete qilish",
        '.append()': "element qoshish",
        '.title()':"bosh xarfi katta bulsin",
        '.upper()': "barcha xarflar katta bulsin",
        '.lowee()':"barcha xarflar kichik bulsin"
        }
print("These the basics what have been covered during this Python course:\n", terms,"\n\n")

#____________________________________________________

#4
en_uz = {
            'apple':"olma",
            'peach':"nok",
            'melon':"qovun",
            'orange': "apelsin",
            'mulberry':"tut"
            }
key = input("Write a fruit name please:").lower()
print(en_uz.get(key,"There is no such fruit on our dictionary"))

key = input("\nWrite a fruit name please:").lower()
translation = en_uz.get(key)
if translation == None:
    print("There is no such fruit on our dictionary")
else:
    print(f"The fruit {key.title()} is translated into uzbek as {translation}")










