from polynomial import *



#Like in the Franklin–Reiter related-message attack, i.e., find the gcd of two polynomials

N= 2157212598407

# Compute g1 = x**3 - c1 mod N
g1 = [1,0,0,-1429779991932]

# Compute g2 = (x+m)**3 - c2 mod N
rel = [1,1024]
g2 = polyMul(rel,rel,N)
g2 = polyMul(g2,rel,N)
g2 = polyAdd(g2,[-655688908482],N)


print("g1 is: ",g1)
print("g2 is: ",g2)

gcdPolynomial = PolyGCD(g2,g1,N)

print("The encrypted message is: ", N-gcdPolynomial[1])





