def calculate_average(data):


 if not data:
   raise ValueError("Data cannot be empty.")

 
 try:
   sum_of_data = sum(data)
 except TypeError:
   raise TypeError("Data must be numeric.")

 return sum_of_data / len(data)


num_inputs = int(input("How many numbers do you want to average? "))
inputs = []
for i in range(num_inputs):
 value = float(input(f"Enter number {i+1}: "))
 inputs.append(value)

average = calculate_average(inputs)
print(f"The average of the numbers you entered is {average}")
