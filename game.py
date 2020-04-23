from random import randint

random_value = randint(1, 50)
print(random_value)

user_name = input("Hey there, my name is Boot, what is yours? ")
print(user_name, " this is how it's gonna work:")
print("You will have 5 chances to guess the secret number that I am thinking of in a range between 1 and 50, got it?")
print("Let's game \n")

user_guess = int(input("So wich number do you have in mind? "))

for i in range(1, 6):

    if (user_guess == random_value):
        print(user_name, "congrats, you've won!")
        break
    elif (user_guess > random_value):
        print("Sorry, I though of a number a little bit smaller")
        print("Attempts made: ", i)
        if (i <=5 ):
            user_guess = int(input("Try again: "))
    else:
        print("Sorry, I though of a number a little bit bigger")
        print("Attempts made: ", i)
        if (i <=5 ):
            user_guess = int(input("Try again: "))