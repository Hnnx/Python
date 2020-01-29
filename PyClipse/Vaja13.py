#asert ne ujame exceptiona ampak ga izpise- se uporavblja za testiranje 
def kelvinFahrenheit(temperatura):
    assert( temperatura >= 0),  "Ne more biti bolj mrzlo od absolutne ničle"
    
    
    fahrenheit = (  (temperatura - 273)  * 1.8) + 32
    return fahrenheit

kelvin = int(input("Vnesi temp v K"))
print("Fahrenheit = ", kelvinFahrenheit(kelvin))