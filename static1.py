import math
class Sample:
    @staticmethod
    def calculate(x):
        result=math.sqrt(x)
        return result
    
    def powercalc(a,b):
        result1=a**b
        return result1

S1=Sample.calculate(128)
print(S1)
S2=Sample.powercalc(5,6)
print(S2)