def are_anagrams(str1, str2):
  """Checks if two strings are anagrams of each other."""

  # Handle case-insensitivity and non-alphanumeric characters:
  str1 = "".join(char.lower() for char in str1 if char.isalnum())
  str2 = "".join(char.lower() for char in str2 if char.isalnum())

  # Efficiently check if characters have the same counts:
  return sorted(str1) == sorted(str2)

# Get user input:
text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")

# Check for anagrams and print result:
if are_anagrams(text1, text2):
  print("The strings are anagrams.")
else:
  print("The strings are not anagrams.")
