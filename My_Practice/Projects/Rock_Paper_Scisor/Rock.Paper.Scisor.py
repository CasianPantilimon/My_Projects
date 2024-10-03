import random

user_score = 0
pc_score = 0

options = ["piatra", "hartie", "foarfece"]

print("\nWelcome to the: Rock, Paper, Scissors game!\n"
      "- To stop the game, type: stop joc\n")

while True:
    pc_choice = random.choice(options)
    user_choice = input("Alege o optiune: ").lower()

    if user_choice == "stop joc":
        print(f"User final score is: {user_score}")
        print(f"PC final score is: {pc_score}")
        if user_score > pc_score:
            print("Felicitari, ai castigat!")
        else:
            print("The game is over. The PC won the game.")
        break

    print(f"PC a ales {pc_choice}\n")

    if user_choice not in options:
        print("Optiune invalida, te rog sa alegi din: piatra, hartie, foarfece.")
        continue

    if user_choice == pc_choice:
        print("Remiza")
    elif (user_choice == "piatra" and pc_choice == "foarfece") or \
         (user_choice == "hartie" and pc_choice == "piatra") or \
         (user_choice == "foarfece" and pc_choice == "hartie"):
        user_score += 1
        print("Ai castigat!")
    else:
        pc_score += 1
        print("PC-ul a castigat!")

