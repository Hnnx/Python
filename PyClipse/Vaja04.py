#Py Array
#String je lahko 'str' ali "STR"

seznam = ['abc', 73, 0.14, "Banana",'abc']
print(seznam)

#Dodamo shit z append
seznam.append("Hruska")

#Remove iz arraya
#abc bo zbrisal PRVI abc (ce jih je vec not)
seznam.remove('abc')
print(seznam)

seznam.remove(seznam[0])
print(seznam)



seznam2 = [1,2,3,4,5]

#Print range
print(seznam2[1:2])


drugiSeznam = ["Jabolko", "jagoda"]

tretjiSeznam = seznam + drugiSeznam

print(tretjiSeznam)


#TUPLE je fixne velikosti in ni mutable, ne mores spreminjat - lahko fliknes v seznam in potem menjujes
tuplic = ("Babana", 123, 0.12344)
print(tuplic)

#MutliArray
multiSeznam = [
                [1,2,3,4],
                ['a','b','c','d']
              ]

print(multiSeznam)
print(multiSeznam[1][1])

multiSeznam2 = [
                [1,2,3,4],
                ["a","b","c"],
                "Banana",
                6666
                ]


print(multiSeznam2)

#Zadnjega ( str.length - 1 )
print(multiSeznam2[-1])


print(multiSeznam2[::-1])


#JSON
leksikon = {'ime':'Marko','priimek':'Devetak','letnica':1984 }
print(leksikon['ime']+" "+ leksikon['priimek'])


#MultiLeksikon
multiLeksikon = {
                    'oseba1':{'ime':'Marko','priimek':'Devetak'},
                    'oseba2':{'ime':'Joze', 'priimek':'Desetak'}
                    }
                    
                    

print(multiLeksikon['oseba2']['ime'])
