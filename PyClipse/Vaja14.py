class Oseba:
    'Razred za delo z osebami'
    stejOsebe = 0
    
    def __init__(self, ime, starost):
        self.ime = ime
        self.starost = starost
        Oseba.stejOsebe += 1
        
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, " uspeno unicen")
        
        
    def izpisiSteviloOseb(self):
        print("Vseh oseb je: ", Oseba.stejOsebe)
        
        
    def izpisiOsebo(self):
        print("Ime: ", self.ime, " Starost: ", self.starost)
        
print("dela")
        