#Guess the Dragon's Secret
def check_guess(secret_number, guess):
    if guess==secret_number:
        print("Congratulations!")
    elif guess>=secret_number:
        print("Too high")
    elif guess<=secret_number:
        print("Too low")
secret_number=7
guess=int(input("Guess the Dragon's secret: "))
check_guess(secret_number, guess)