print(2+2)
intVar = 1
floatVar = 3.14
booleanVar = False
stringVar = "slowo"
pustyVar = None

print(intVar, floatVar, booleanVar, stringVar, pustyVar)

print(type(intVar))

print(type(2+2.0))

if 2 is 2: 
    print("warunek jest spełniony")
else:
    print("warunek nie jest spelniony")
def setup():
    pass
    
def draw():
    print(mousePressed)#jezeli mysz wcisnieta
    line(20, 30, 90, 160)#dopiero to rysuj
    #a jesli nie wcisnieta
    #to zadziej cos innego