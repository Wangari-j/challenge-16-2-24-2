#1st step is to create a class
class Calculator:
    num1 = 10
    num2 = 5


    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addCalc(self):
        #if we want to accesss class attribute in class methods, we have to prefix the attribute with -self. e.g self.num1

        result = self.num1 + self.num2
        return result
    
    def subFunc(self):
        result = self.num1 - self.num2
        return result
    
    def multiplyFunc(self):
        result = self.num1 * self.num2
        return result
    
    def divisionFunc(self):
        result = self.num1//self.num2
        return result
    
#2nd step: we create the first class object. If the class has 'init' we pass attribute.
    
calc1 = Calculator(10,5)
calc2  = Calculator(200,100)
#step 3: We can call the class methods

print(calc1.addCalc())

print(calc1.subFunc())
print(calc1.multiplyFunc())
print(calc1.divisionFunc())

print(calc2.multiplyFunc())
print(calc2.addCalc())