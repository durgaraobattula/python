def swap_case(str1):
  res = ''.join(chr(ord(c) ^ 32) if c.islower() else c for c in str1)
  return res
str1 = "apple"
swapped_string = swap_case(str1)
print(swapped_string)
