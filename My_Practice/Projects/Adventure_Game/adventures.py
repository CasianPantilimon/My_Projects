print("Welcome to a game the never ending adventures... hopefully ;)\n")

name = input("What is your name, brave player: ").capitalize()
print(f"Welcome {name}, to the adventure game that never ends... hopefully 🔪\n")

print(
    "You have been on the road for many days, weary and hungry. Your supplies ran out long ago, "
    "and the sun beats down on you mercilessly. Just as you feel you cannot take another step, "
    "you see a dense forest in the distance. With renewed hope, you head towards the trees, "
    "hoping to find food and water. As you enter the forest, you come upon a crossroad.\n"
)

direction = input("Would you like to go left or right? ").lower()

if direction == "left":
    print("\nWHOOOOOO! You found a pack of ducks. You catch them and fry them up, "
          "restoring your strength. To your surprise, these ducks were magic. "
          "You now have the power to fly, but it won't last forever.\n")

    direction = input("Would you like to fly over the forest and get out of there, "
                      "or stay in the forest hoping for more twisted adventures? "
                      "Type 'fly' to fly away or 'stay' to stay in the forest: ").lower()

    if direction == "stay":
        print(f"\nWoow, you lazy adventurer. Instead of seizing the opportunity, you choose to stay. "
              f"As you settle down to rest, you notice a faint light flickering through the trees. "
              "You follow it and discover an ancient, abandoned cabin. Inside, you find a dusty old book "
              "filled with mysterious runes and symbols.\n")

        choice = input(
            "Do you want to try and decipher the book or leave it alone? "
            "Type 'read' to read the book or 'leave' to leave it alone: ").lower()

        if choice == "read":
            print(
                f"\nAs you start to read the book, the runes glow and the cabin shakes. "
                f"A hidden door opens, revealing a secret passage. "
                f"Bravely, you step inside and find yourself in an underground labyrinth filled with "
                f"treasures beyond your wildest dreams. "
                f"Congratulations, {name}! YOU WIN! 🎉")
        elif choice == "leave":
            print(
                f"\nYou decide it's best not to meddle with unknown magic. "
                f"You leave the cabin and continue exploring the forest, "
                f"always wondering what secrets the book held. NO MORE ADVENTURES FOR YOU, {name} 🔪")
        else:
            print(
                f"\nThat was not a valid choice. However, since you are so determined to go '{choice}', "
                f"FINE, I will take you. "
                f"You wander for many days looking for '{choice}', get bored and go home.\nNO MORE ADVENTURES FOR YOU!")
    elif direction == "fly":
        print(f"\nWoow, you lazy adventurer. Instead of using your newfound power, you choose to fly away. "
              "As you soar above the treetops, you spot a glimmering lake in the distance. "
              "You decide to land and explore.\n")

        choice = input(
            "At the edge of the lake, you find a small boat tied to a post. "
            "Do you want to take the boat and explore the lake, "
            "or stay on the shore and rest? Type 'boat' to take the boat or 'rest' to stay on the shore: ").lower()

        if choice == "boat":
            print(
                f"\nYou untie the boat and row out onto the lake. The water is calm and clear, and you feel at peace. "
                "Halfway across the lake, you see a small island with a single, towering tree. "
                "You row to the island and discover a chest filled with gold and jewels at the base of the tree. "
                f"Congratulations, {name}! YOU WIN! 🎉")
        elif choice == "rest":
            print(f"\nYou decide to stay on the shore and rest. As you lay down, you hear rustling in the bushes. "
                  "A group of forest creatures emerges, offering you food and drink. "
                  "You spend a pleasant evening with them, but eventually, you must move on. "
                  "NO MORE ADVENTURES FOR YOU, {name} 🔪")
        else:
            print(
                f"\nThat was not a valid choice. However, since you are so determined to go '{choice}', "
                f"FINE, I will take you. "
                f"You wander for many days looking for '{choice}', get bored and go home.\nNO MORE ADVENTURES FOR YOU!")
    else:
        print(
            f"\nThat was not a valid choice. However, since you are so determined to go '{direction}', "
            f"FINE, I will take you. "
            f"You wander for many days looking for '{direction}', get bored and go home.\nNO MORE ADVENTURES FOR YOU!")

elif direction == "right":
    print("\nAfter crossing the dense forest, you come upon a vast river. "
          "You eat well from the provisions you found and overcome your childhood fear of the full moon.\n")

    direction = input(f"Time to move forward, {name}. Would you like to cross the mighty river or walk around it? "
                      "Type 'swim' to swim across or 'walk' to walk around it: ").lower()

    if direction == "swim":
        print(f"\nA tiny alligator bites one of your toes. You panic and drown. NO MORE ADVENTURES 🔪")
    elif direction == "walk":
        direction = input(
            "\nYou come to a bridge. It looks wobbly. "
            "Do you want to cross it? Type 'yes' to cross or 'no' to find another way: ").lower()

        if direction == "yes":
            print(f"\nYou bravely step onto the bridge. It creaks and sways, but you make it across safely. "
                  f"On the other side, you find a hidden treasure chest filled with gold and jewels! "
                  f"Congratulations, {name}! YOU WIN! 🎉")
        elif direction == "no":
            print(
                f"\nYou decide to find another way. After hours of searching, you find a sturdy path around the river. "
                f"Exhausted but safe, "
                f"you continue your journey and discover a peaceful village where you decide to settle. "
                f"NO MORE ADVENTURES FOR YOU, {name} 🔪")
        else:
            print(
                f"\nThat was not a valid choice. However, since you are so determined to go '{direction}', "
                f"FINE, I will take you. "
                f"You wander for many days looking for '{direction}', get bored and go home."
                f"\nNO MORE ADVENTURES FOR YOU!")
    else:
        print(
            f"\nThat was not a valid choice. However, since you are so determined to go '{direction}', "
            f"FINE, I will take you. "
            f"You wander for many days looking for '{direction}', get bored and go home.\nNO MORE ADVENTURES FOR YOU!")

else:
    print(
        f"\nThat was not a valid direction. However, since you are so determined to go '{direction}', "
        f"FINE, I will take you. "
        f"You wander for many days looking for '{direction}', get bored and go home.\nNO MORE ADVENTURES FOR YOU!")
