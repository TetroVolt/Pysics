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
            tot += eval(each)
        return tot


class FuncParser:
    def __init__(self, str):
        self.part = self.parser(str)

    def parser(self, str):
        str = self.removeSpaces(str)
        L = []
        for elm in self.kesSplit(str):
            elm = self.replaceX(elm)
            elm = elm.replace('^', '**')
            L.append(elm)
            first = False
        return L

    def kesSplit(self, str):
        L1, ret = self.specialMinusSplit(str), []
        for sec in L1:
            for each in sec.split('+'):
                ret.append(each)
        return ret

    #resurns a list of seperated parts
    def specialMinusSplit(self, str):
        indexList = [i for i in range(len(str)) if str[i] == '-']
        lastIndex = 0
        retList = []
        for index in indexList:
            if index==0:
                continue
            if str[index-1].isdigit() or str[index-1]=='x':
                retList.append(str[lastIndex:index])
                lastIndex = index
        retList.append(str[lastIndex:])
        return retList

    def replaceX(self, str):
        indexList = [i for i in range(len(str)) if str[i] == 'x']
        retStr = ''
        lastIndex = 0
        for index in indexList:
            if index == 0:
                continue
            if str[index-1].isdigit() or str[index-1] == ')':
                retStr += str[lastIndex:index]
                lastIndex = index
        retStr += str[lastIndex:]
        return retStr


    def removeSpaces(self, str):
        cstr = []
        for char in str:
            if char != ' ':
                cstr.append(char)
        return ''.join(cstr)
