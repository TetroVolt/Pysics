#Integrals/Derivatives
class Polynomial:
    def __init__(self, L):
        #for now a polynomial is treated as a List of the coeficients from highest to lowest.
        #This means that len(L) - 1 is the degree of the Polynomial
        self.coef = L
    def integrate(self, a, b):
        i, tot = a, 0
        delta = .00001
        length = len(self.coef)
        while i < b:
            for o in range(length):
                ex = length - o - 1
                tot += self.coef[o] * (i ** ex) * delta
            i+=delta
        return tot
