#    import string
#    print(list(string.ascii_letters))
#    print(string.digits)
#    print(string.punctuation)
import random
word_bank = ["mailman", "lemon", "speaker", "peach", "tricycle",
             "night", "bike", "yellow", "mothman", "hippopotamus"]
turns_taken = 0
remaining_guesses = 8
letters_used = []
correct_guesses = []
wrong_guesses = []
chosen_word = word_bank[random.randint(0, 9)]
chosen_word_letters = list(chosen_word)
guessed_letter = []
chosen_word = chosen_word.lower()
for i in range(0, len(chosen_word)):
    word_bank.append("*"*len(chosen_word))
    chosen_word = "*" * len(chosen_word)
#    if letters_used in chosen_word:
#    if letter.upper() == _.upper():
#   chosen_word = "*"*len(chosen_word)
print(chosen_word)
letters_used = input("Guess a letter. ").lower()
guessed_letter.append(letters_used)
