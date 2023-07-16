import random
from hangman_words import word_list
from hangman_art import stages, logo
print(logo)


word_chosen = random.choice(word_list).lower()
print(word_chosen)
display = [] #empty list with "_" empty spaces

for _ in word_chosen:
    display += "_"
print(f"{' '.join(display)}")

end_of_game = False
lives = 6

while not end_of_game:
    guess_letter = input("\n\nEnter your letter! : ").lower()
    if guess_letter in display:
        print(f"You've already guessed this letter, please enter another one.")

    for pos in range(0, len(word_chosen)):
        if word_chosen[pos] == guess_letter:
            display[pos] = word_chosen[pos]
            
    print(f"Your current word :- {' '.join(display)}")
    print(f"\nYou are left with {lives - 1} lives only.")
    
    if guess_letter not in word_chosen:
        lives -= 1
        print("\nYou've entered the wrong leter, now you will lose A life.")
        if lives == 0:
            end_of_game = True
            print("\nTHE MAN GOT HUNGED, YOU LOSE!")
            
    if "_" not in display:
        end_of_game = True
        print("\nYOU SAVED THE MAN, YOU WIN!")
    print(stages[lives])

