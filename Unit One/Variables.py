def get_guess():
    guess = int(input("Enter a guess: "))
    return guess

def main():
    guess = get_guess()
    if guess == 30:
        print("Correct!")
    else:
        print("Incorrect!")
    print(guess)

main()