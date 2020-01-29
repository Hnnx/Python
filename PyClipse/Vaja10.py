'''
r = READ
a = APPEND (dodaja stringe)
w+ = pisanje - ce datoteka ne obstaja jo naredi
r+ = odpri datoteko in beri/pisi
a+ = APPEND (pisi od konca napreja, ce datoteka ne obstaja jo naredi)

'''

datoteka = open("besedilo.txt", "r+")


print("Ime Datoteke: ", datoteka.name)

datoteka.write("Dober dan!\nDanes je lep dan")


print("#datoteka.read(10) = 10 znakov in izpisi, ce damo brez argumenta bere do konca")
print()



# .READ TO BO PREMAKNILO KURZOR ZATO NE BO DELAL FOR IN  OSTALI READI
niz = datoteka.read()
print("Vsebina datoteke: ", niz)

print()
print("readline bere vrstico, readlines pa jih da v nek array")
print("datoteka.readine(x)  x = stevilo vrstic")
print()


#niz = datoteka.readline(2)
#print("Beri naprej", niz)

for vrstica in datoteka:
    print(vrstica)

datoteka.close();