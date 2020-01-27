seznam = [1,2,3,4,5,6,7,8,9,10]

#ITER metoda sprejme seznam in shrani v iteracija "object"
iteracija = iter(seznam)

#Next klice naslednji "element" 
print("Next:")
print(next(iteracija))
print(next(iteracija))
print(next(iteracija))
print(next(iteracija))
print("\n")

#For loop 
print("Obicni for")
for stevilo in seznam:
    print(stevilo)
    
print("\n")
        
#"locilni" znak med elementi
print("Locevanje z vejco (end=\", \") ")
for stevilo in seznam:
    print(stevilo, end=", ")
    
print("\n")

#nadaljuje od 4 dalje, ker smo 4x ze dali NEXT
print("nadaljevanje iteracije")
for stevilo in iteracija:
    print(stevilo)
    

#input
#primerjamo lahko samo stevila! ( == za primitive,   .equals za object)

vnos = input("Vnesi stevilo: ")
st = int(vnos)
if(st <= 100):
    print("Vneseno steviko je manjse ali enako 100")
else:
    print("Stevilo je vecjeod 100")