#The Gate of Numbers
def check_even_odd(number):
    if number%2==0:
        print (f"{number} is even.")
    else:
        print (f"{number} is odd.")
num=input("Provide any integer of your choice ")
while isinstance(num, int)==False:
    if isinstance(num, int)==False:
        print("The number should be an integer")
        num=input("Input an integer number ")
    else:
            break
print(check_even_odd(num))        