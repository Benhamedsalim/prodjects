import random
employees = ['hassan', 'hadi', 'salim', 'ahmed']
winner = random.choice(employees)
x = ['_'] * len(winner)
print(' '.join(x))
time = 12
guessed = []
while time > 0 and "_" in x:
    name = input("Enter your letter: ").lower()
    if name in guessed:
        print("You already guessed this letter")
        print(f"You have {time} guesses ")
        continue
    else:
        guessed.append(name)
    if name not in winner:
        time = time - 1
    else:
        for i in range(len(winner)):
            if winner[i] == name:
                x[i] = name
    print(' '.join(x))
    print(f"You have {time} guesses ")

if time == 0:
    print("""
    ***********
    YOU LOSE
    ***********
    """)
else:
    print("""
        ***********
          YOU Win
        ***********
        """)
