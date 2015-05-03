<<<<<<< HEAD
t1 = "Hallo Welt"
t2 = 'Auch das ist eine Zeichenkette'
t3 = """Diese Zeichenkette
        geht über mehrere
        Zeilen"""
t4 = 'hier sind "Doppelte Hochkommata" gespeichert'
print ("bitte geben Sie einen TExt ein")
t5 = input()
print ("t1:",t1)
print ("t2:",t2)
print ("t3:",t3)
print ("t4:",t4)
print ("t5:",t5)

print ("Typ:",type(t1))
=======
import fractions

z = 12
n = 28

print("Bruch",z,"/",n)

#als fraction
b1 = fractions.Fraction(z,n)
print("FRaction:",b1)
print("Z, N:",b1.numerator,b1.denominator)
wert = b1.numerator / b1.denominator
print("WERT:",wert)
print()

#umrechnen
x=2.375
print("Zahl",x)
b2 = fractions.Fraction(x)
print("Fraction:",b2)
print()

print("Bruch",z,"/",n)
print("ggT",fractions.gcd(z,n))
>>>>>>> b14e4a7efbd060f8159d7685fdd937cbeb694ac4
