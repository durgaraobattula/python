def add(num1, num2):
    
    if not num2:  
        return num1
    else:
        carry = (num1 & num2) << 1 
        sum_without_carry = num1 ^ num2  
        return add(sum_without_carry, carry)  
def subtract(num1, num2):
    
    while num2 != 0:  
        borrow = (~num1) & num2  
        diff = num1 ^ num2 
        num1 = diff  
        num2 = borrow << 1  
    return num1


num1 = 10
num2 = 5

sum = add(num1, num2)
print("Sum:", sum)  

difference = subtract(num1, num2)
print("Difference:", difference)  