seznam = [1,2,3,4,5,6,7,8,9,10]


#ITER metoda sprejme seznam in shrani v iteracija "object"
iteracija = iter(seznam)


#Next klice naslednji "element" 
print(next(iteracija))
print(next(iteracija))
print(next(iteracija))
print(next(iteracija))


#Python for
for stevilo in seznam:
    print(stevilo)