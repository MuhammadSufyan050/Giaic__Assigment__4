import hashlib

def has_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

store_logins = {
    "abc@sample.com":has_password("password123"),
    "admin@example.com":has_password("adminpass")
}

def login(email,password):
    if email in store_logins:
        return store_logins[email] == has_password(password)
    return False

if __name__ == "__main__":
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, password):
        print("Login successful!")
    else: 
        print("Invalid email or password.")