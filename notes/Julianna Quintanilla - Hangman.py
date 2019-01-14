import random
word_bank = ["Mailman", "lemon", "speaker", "peach", "Tricycle", "night",
             "I have a red bike.", "yellow", "Mothman", "hippopotamus"]
turns_taken = 0
remaining_guesses = 8
letters_used = []
correct_guesses = []
chosen_word = word_bank[random.randint(0, 9)]
for i in range(0, len(chosen_word)):
    correct_guesses.append("*")
