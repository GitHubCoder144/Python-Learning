def main():
    difficulty = input("Difficult or Casual").strip()
    try:
        amount_of_players = int(input("How many players would you like to play? "))
    except ValueError:
        print("Please enter a number.")
        return

    if difficulty == "Difficult":
        if amount_of_players >= 1:
            if amount_of_players > 1:
                recommend("bridge or poker")
            else:
                recommend("Spider Solitaire or Yukon")
        else:
            print("Enter A Valid Number")
    elif difficulty == "Casual":
        if amount_of_players >= 1:
            if amount_of_players > 1:
                recommend("UNO or Exploding Kittens")
            else:
                recommend("Klondike or Pyramid")
        else:
             print("Enter A Valid Number (1 or More)")
    else:
         print("Choose either 'Difficult' or 'Casual'.")


def recommend(game):
    print("You might like", game)


main()