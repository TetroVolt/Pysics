#Integrals/Derivatives
from math import sin, cos, tan, pi
class Function:
    def __init__(self, parsed):
        self.part = parsed.part
    def integrate(self, a, b):
        x, tot = a, 0
        delta = .0001
        while x < b:

            tot += (eval(self.part) * delta)
            x+=delta
        return tot
    def slopeAt(self, x):
        diff, delta = 0, .0000000001
        temp = each.replace('x', '(x+delta)')
        diff += (eval(temp) - eval(self.part)) / delta
        return diff
    def evaluateAt(self, x):
        tot = 0
        tot += eval(self.part)
        return tot


class FuncParser:
    def __init__(self, str):
        self.part = self.parser(str)

    def parser(self, str):
        str = self.removeSpaces(str)
        str=self.replaceX(str)
        str=str.replace('^', '**')
        return str

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
        lastIndex = indexList[0]
        retStr = str[:lastIndex]
        for index in indexList:
            if index == 0:
                continue
            if str[index-1].isdigit() or str[index-1] == ')':
                retStr += ('*' + str[lastIndex:index])
                lastIndex = index
        retStr += '*' + str[lastIndex:]
        return retStr


    def removeSpaces(self, str):
        cstr = []
        for char in str:
            if char != ' ':
                cstr.append(char)
        return ''.join(cstr)
x = Function(FuncParser("3x^3-10x^x+9x"))
print(x.integrate(0,1))
