from Vaja6 import izracun

#charAt varianta - string z "for each" loopom

niz = "Banana"

for crka in niz:
    print(crka)
    
print()
    

#obicni while
i = 0
while (i < 10):
    print("i = ", i)
    i += 1
    
    
print()
    
a = 0
#Obicni For - zacne z 0 in NE gre do 11 
for stevilo in range(0,11):
    a += 1
    print(stevilo)



print("Loop gre do 10, a se bo incremental do 11")
print(a)

print()
print("Defalut values - sestej(a, b= 4)")
def sestej(a, b = 4):
    return a+b

print("Sestej(5)   (a+4)")

izracun = sestej(5)
print(izracun)
print("Sestej (3,10)")

izracun = sestej(3,10)
print(izracun)
    
    
