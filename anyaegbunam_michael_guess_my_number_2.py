import random

def main():
    
    random_number = random.randint(1, 100)

    print("I have generated a random number between 1 and 100. You have will 10 attempts to guess that number.")

    for attempts in range(1, 11):
        guess = int(input(f"Attempt {attempts}: guess: "))

        if guess == random_number:
            print(f"You guessed my random number.")
            break
        elif guess < random_number:
            print("Your guess is less than my random number. Try again")
        else:
            print("Your guess is higher than my random number. Try again")

if __name__ == "__main__":
    main()

  
