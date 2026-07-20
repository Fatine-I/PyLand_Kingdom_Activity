#Login Credentials
def login(username, password):
    username="admin"
    password="python123"    
u=input("Enter the Username ")
p=input("Enter the password")
verification=login(u,p)
if not verification:
    print("Access Denied!")
else:
    print("Login Successful!")

