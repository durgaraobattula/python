import bcrypt 

def create_authenticator(username, password):
    

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return username, hashed_password

def authenticate(username, password, stored_credentials):
   

    stored_username, stored_hashed_password = stored_credentials
    if username != stored_username:
        return False
    return bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password)


credentials = create_authenticator("john", "mypassword123")
print(credentials)  
if authenticate("john", "mypassword123", credentials):
    print("Authentication successful!")
else:
    print("Authentication failed.")
