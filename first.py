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
