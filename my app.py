# Bank App

# File to store user information

def sign_up():
    global account_name 
    global password 
    print("===== Sign Up =====")
    account_name = input("Enter your account_name: ")
    password = input("Enter your password: ")
    confirm = input ("Re-enter password: ")

    if password == confirm: 
        print("Sign up successful.")
    else:
         print("Re-confirm.")
         sign_up()

def login():
    print("===== Login =====")
    login_account_name = input("Enter your username: ")
    login_password = input("Enter your password: ")

    if account_name == login_account_name and password == login_password:
        print("Logn successful.")
    else:
        print("Invalid account_name or password.")
        login()
        
        
        
sign_up()
login()

