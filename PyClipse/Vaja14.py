class Oseba:
    'Razred za delo z osebami'
    stejOsebe = 0
    
    #Vse metode imaj ovsaj 1 parameter - self (this je v javi)
    #INIT JE KONSTRUKTOR
    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost
        Oseba.stejOsebe += 1
    
    #DESTRUKTOR
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, " uspeno unicen")
        
        
    #METODE
    def izpisiSteviloOseb(self):
        print("Vseh oseb je: ", Oseba.stejOsebe)
        
        
    def izpisiOsebo(self):
        print("Ime: ", self.ime, " Starost: ", self.starost)

oseba1 = Oseba("Janez" , 20)
oseba2 = Oseba("Lojze", 34)
oseba3 = Oseba("Jure", 55)


oseba1.izpisiOsebo()
oseba2.izpisiOsebo()

print("Ime:", oseba3.ime)
print("Stevilo vseh oseb: ", Oseba.stejOsebe)
print("")

del oseba3

print(Oseba.__doc__)
