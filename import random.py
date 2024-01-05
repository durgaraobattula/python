import random
import string

def generate_password():
    

    
    characters = string.ascii_letters + string.digits + string.punctuation

    
    password = "".join(random.choice(characters) for _ in range(16))

    return password


password = generate_password()
print(f"Generated password: {password}")
