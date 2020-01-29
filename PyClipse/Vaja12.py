from _ast import Try
try:
    datoteka = open("test.txt", "w")
    datoteka.write("Testno besedilo")
    
#Uporabimo """ za stringe ki jih bomo locli z odstavki    
except IOError:
    print("""Napaka pri pisanju v datoteko je 
    prislo do napake""")
else:
    print("Pisanje v datoteko uspelo")
    
finally:
    datoteka.close()
    
    
'''
    try/catch/finally tle zgleda:
    
    Try
    except 
    else
    finally
    
'''