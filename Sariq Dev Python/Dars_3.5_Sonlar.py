# int() - butun son ;
# float() - o`nlik son ;
# str() - matn
a = 3
b = 4
c = (a**2+b**2)**0.5
print ("C equals = ",c,"\n")

X, Y, Z = 5.5, -3, 6
yigindi= X+Y+Z
print("Summa = ",yigindi,"\n")
age, name, prof = 35, "george", "teacher"
print(f"{age} year old {name.title()} is working as a {prof} in the school.\n")


#yosh str emas balki int bulgani uchun consolega chiqarish vaqtida unga str() buyrugini berib consolega chiqarib oldik
ism = "David"
vozrast = 18
xabar = ism+ " "+ str(vozrast)+ " yoshda" 
print(xabar)

t_yil = int(input("Tug`ulgan yilingizni kiriting: \n>>>"))
yosh = 2023 - t_yil
print("Siz demak ", yosh," yoshda ekansiz")






