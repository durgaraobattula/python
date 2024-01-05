def outer_function(num):
    
    def inner_function(multiplier):
        
        return num * multiplier

    
    return inner_function


double_function = outer_function(5)


result = double_function(2)
print(f"Double of 5 is: {result}")  


triple_function = outer_function(3)
print(f"Triple of 3 is: {triple_function(3)}")  
