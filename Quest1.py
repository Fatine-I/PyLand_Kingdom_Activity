#The Gate of Numbers
def check_even_odd(number):
    if number%2==0:
        print (f"{number} is even.")
    else:
        print (f"{number} is odd.")
try:        
    num=int(input("Provide any integer of your choice "))
    
except ValueError as e:
    print("The number is not an integer")  
print(check_even_odd(num)) 