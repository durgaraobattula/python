def is_palindrome(text):
  """
  Checks whether the given text is a palindrome or not.

  Args:
      text: The text to be checked.

  Returns:
      True if the text is a palindrome, False otherwise.
  """

  # Preprocess the text:
  text = "".join(char for char in text.lower() if char.isalnum())

  # Check for palindrome:
  return text == text[::-1]

# Get user input:
text = input("Enter a string: ")

# Check for palindrome and print result:
if is_palindrome(text):
  print(f"'{text}' is a palindrome.")
else:
  print(f"'{text}' is not a palindrome.")
