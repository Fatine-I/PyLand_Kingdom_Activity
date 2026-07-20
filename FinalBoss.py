#Login Credentials
username="admin"
password="python123"
def login(un, pw):       
    if (un,pw)!=(username,password):
        print("Access Denied!")
    else:
        print("Login Successful!")
u=input("Enter the Username ")
p=input("Enter the password ")
login(u,p)
