"""
Rules:
- ask the user a bunch of questions
- for every right answer the user will get a point
- at the end print the score

Questions:
1. What is always coming but never arrives?

tomorrow
2. What word is spelled incorrectly in every single dictionary?

incorrectly

3. What is it that lives if it is fed, and dies if you give it a drink?

fire
4. What never asks a question but gets answered all the time?

cellphone

5.Is the tomato a fruit or a vegetable?
vegetable

"""
print("This is a quizz game.")
permission = input(
    "Would you like to play it?:"
    "\n -Yes: Mark me asintriggered! "
    "\n -No: What a waste of time... "
    "\n Your answer: ").lower()
if permission != "yes":
    quit()
print("⚡⚡⚡ Welcome to my quick quizz game! ⚡⚡⚡")
score = 0
correct_answers = ["tomorrow", "incorrectly", "fire", "phone", "vegetable", ]
print(score, "initial score")
answers = []
q1 = input("1. What is always coming but never arrives?🤔 ").lower()
answers.append(q1)
q2 = input("2. What word is spelled incorrectly in every single dictionary?🤓 ").lower()
answers.append(q2)
q3 = input("3. What is it that lives if it is fed, and dies if you give it a drink?😎 ").lower()
answers.append(q3)
q4 = input("4. What never asks a question but gets answered all the time? ").lower()
answers.append(q4)
q5 = input("5.Is the tomato a fruit or a vegetable?🍆 ").lower()
answers.append(q5)

for i in answers:
    if i == "tomorrow":
        score += 1
    if i == "incorrectly":
        score += 1
    if i == "fire":
        score += 1
    if i == "phone":
        score += 1
    if i == "vegetable":
        score += 1
# sa afisez raspunsurile
print("\n- Your answers were: ")
for idx, ya in enumerate(answers):
    print(ya)

print("\n- The correct answers were:")
for idx, ca in enumerate(correct_answers):
    print(ca)

# print(score, "updated score")
print("🏁 🏁 🏁 Final score is: 🏁🏁 🏁 \n ")
if score == 1:
    print(f"You answered correctly {score / 4 * 100}% of the above questions\n🙁🙁")
if score == 2:
    print(f"You answered correctly {score / 4 * 100}% of the above questions\n")
if score == 3:
    print(f"You answered correctly {score / 4 * 100}% of the above questions\n 🙌 🙌 🙌 🙌")
if score == 4:
    print(f"You answered correctly {score / 4 * 100}% of the above questions\n 🎉🎉🎉🎉🎉🎉")
if score == 5:
    print(f"You answered correctly {score / 4 * 100}% of the above questions\n🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳")
