#The Village of Ages
def age_category(age):
    if 0<=age<=12:
        return "Child"
    elif 13<=age<=19:
        return "Teenager"
    elif 20<=age<=59:
        return "Adult"
    elif 60<=age:
        return "Senior"
User_age=int(input("Your age:"))        
print(age_category(User_age))        