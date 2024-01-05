class Calculator:
    

    def add(self, num1, num2):
        
        return num1 + num2

    def subtract(self, num1, num2):
        
        return num1 - num2

    def multiply(self, num1, num2):
        
        return num1 * num2

    def calculate(self, operation, num1, num2):
        
        if operation == "+":
            return self.add(num1, num2)
        elif operation == "-":
            return self.subtract(num1, num2)
        elif operation == "*":
            return self.multiply(num1, num2)
        else:
            return "Invalid operation."


calculator = Calculator()
result = calculator.calculate("+", 5, 3)
print("5 + 3 =", result)  

result = calculator.calculate("-", 10, 4)
print("10 - 4 =", result)  

result = calculator.calculate("*", 7, 2)
print("7 * 2 =", result)  


result = calculator.add(4, 5)  
print("4 + 5 =", result)    