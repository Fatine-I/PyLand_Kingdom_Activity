#Check result(mark)
def check_result(mark):
    if mark>=50:
        print("Pass")
    else:
        print("Fail")     
m=int(input("What are your marks? "))
if not 0<=m<=100:
    raise ValueError(f"invalid mark!\n marks should range between 0 and 100")
print(check_result(m))