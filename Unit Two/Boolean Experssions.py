def recommend(game):
    print("You might like", game)

def main():
    difficulty = input("Hard or Easy?")

    if difficulty != "Hard" and difficulty != "Easy":
        print("Please enter a difficulty.")
        return

    amount_of_players = int(input("How many players? "))
    if not (amount_of_players >= 1):
        print("Please enter a valid number of players.")
        return

    if difficulty == "Hard":
        if amount_of_players >= 1:
            if amount_of_players > 1:
                recommend("bridge or poker")
            else:
                recommend("Spider Solitaire or Yukon")
    elif difficulty == "Easy":
        if amount_of_players >= 1:
            if amount_of_players > 1:
                recommend("UNO or Exploding Kittens")
            else:
                recommend("Klondike or Pyramid")

main()