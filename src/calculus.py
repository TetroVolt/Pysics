#Integrals/Derivatives
from math import sin, cos, tan, pi
class Function:
    def __init__(self, parsed):
        #for now a polynomial is treated as a List of the coeficients from highest to lowest.
        #This means that len(L) - 1 is the degree of the Polynomial
        self.part = parsed.part
    def integrate(self, a, b):
        x, tot = a, 0
        delta = .0001
        while x < b:
            for each in self.part:
                tot += (eval(each) * delta)
            x+=delta
        return tot
    def slopeAt(self, x):
        diff, delta = 0, .0000000001
        for each in self.part:
            temp = each.replace('x', '(x+delta)')
            diff += (eval(temp) - eval(each)) / delta
        return diff
    def evaluateAt(self, x):
        tot = 0
        for each in self.part:
            print(each, x, eval(each))
            tot += eval(each)
        return tot


class FuncParser:
    def __init__(self, str):
        self.part = self.parser(str)
    def parser(self, str):
        str = self.removeSpaces(str)
        print(str)
        L = []
        first = True
        for elm in self.kesSplit(str):
            index = elm.find('x')
            if not first and index >= 0 and (elm[index-1].isdigit() or elm[index-1] == ')'):
                elm = elm.replace('x', '*x')
            elm = elm.replace('^', '**')
            L.append(elm)
            first = False
            print(L)
        return L

    def kesSplit(self, str):
        L1, ret = str.split('-'), []
        for i in range(1, len(L1)):
            L1[i] = '-' + L1[i]
        for sec in L1:
            for each in sec.split('+'):
                ret.append(each)
        return ret

    def specialMinusSplit(self, str):
        pass

    def removeSpaces(self, str):
        cstr = []
        for char in str:
            if char != ' ':
                cstr.append(char)
        return ''.join(cstr)
