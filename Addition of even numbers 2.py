def add_even_numbers():
  
  num_inputs = int(input("How many numbers do you want to add? "))
  sum_of_even_numbers = 0

  for i in range(num_inputs):
    value = int(input(f"Enter number {i+1}: "))
    if value % 2 == 0:  # Check if the number is even
      sum_of_even_numbers += value

  print(f"The sum of the even numbers you entered is {sum_of_even_numbers}")

add_even_numbers()