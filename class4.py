class Calculator:
    def add(self, a, b, c=0):
        return a+b+c

class AdvancedCalculator(Calculator):
    def add(self, *args):
        return sum(args)
    
calc = Calculator()
print("sum with two parameters (2, 3): ",calc.add(2,3))
print("Sum with three parameters (10, 20, 30): ", calc.add(10, 20, 30))


adv_calc = AdvancedCalculator()
print("Sum with any number of parameters (1,2,3,4,5):", adv_calc.add(1,2,3,4,5))
print("Sum with three parameters(1,2,3):", adv_calc.add(1,2,3))