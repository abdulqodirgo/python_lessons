# set()
fruits = ['apple', 'banana', 'orange', 'appricot', 'apple', 'banana', 'orange', 'apple', 'carrot']
fruits = set(fruits)
print(f"In the beginning fruits was list but now it turned into 'set ()' format: \n{fruits}\n\n")

# adding one element to the set:
fruits.add('mulberry')

#adding multiple elements to the set:
fruits.update(['onion','watermelon', 'cherry'])
print(fruits,"\n\n")
    
#removing elements from the set:    
fruits.discard("onion")
fruits.discard('carrot')
print(fruits,"\n\n")

#workings on two sets simultaneously:

X = {43,54,12,77,34,87}
Y = {43,54,12,26,51,63}
#unifying two sets
Z = X|Y
#or
Z = X.union(Z)
print(Z)

#highlighting mutual same elements of two sets:
print(X&Y)
print(X.intersection(Y))

#finding symmetric difference from two sets:
print(X^Y)
print(X.symmetric_difference(Y))








