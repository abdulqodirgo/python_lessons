#Upper and Lower methods
ism="Abdulqodir"
familiya="Gofurov"
ism_sharif=f"{ism} {familiya}"
#.upper
print(ism_sharif.upper())#matnni consoleda katta harfda yozishlik

#.upper for variable change
ism_sharif=ism_sharif.upper() #bu holatda Variable Explorer sectionda ism_sharif qiymati ham endi katta xarfda buldi

#.lower
print(ism_sharif.lower()) #consoleda matnni kichik xarfda yozishlik

#.titled
print(ism_sharif.title()) #tekstning hamma so`zdagi birinchi xarflari

#capitalized
print(ism_sharif.capitalize())#takstning birinchi so`zning birinchi xarfi 

#strip, rstrip, lstrip
meva="\t    APPLE    "
print(meva)
print("My favorite fruit is "+meva+" and it very delicious.")#APPLE sozini 2 tomonida boshliq bor

#lstrip
print("My favorite fruit is "+meva.lstrip() +" and it very delicious.") #APPLE sozidan keyin left tomondan boshliq yoqtildi

#rstrip
print("My favorite fruit is "+meva.rstrip() +" and it very delicious.") #APPLE sozidan keyin right tomondan boshliq yoqtildi

#strip
print("My favorite fruit is "+meva.strip() +" and it very delicious.") #APPLE sozidan keyin left and right tomondan boshliq yoqtildi
















