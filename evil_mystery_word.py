# make sure to get an single alpha character.
def is_valid_guess(guess):
        if len(guess) != 1:
            print("Please guess a single letter.")
            return False
        elif not guess.isalpha():
            print("Please guess a valid letter.")
            return False
        elif guess in guessed_letters:
            print("You've already guessed that letter.")
            return False
        else:
            return True

# Define a function to categorize words based on the presence of a specific letter
def categorize_words(words, letter):
    categories = {f"Words with '{letter}' in position {i}": [] for i in range(len(max(words, key=len)))}
    categories[f"Words without '{letter}'"] = []

    for word in words:
        word = word.strip().lower()  # Clean the word and convert to lowercase
        if letter in word:
            for i, char in enumerate(word):
                if char == letter:
                    categories[f"Words with '{letter}' in position {i}"].append(word)
                    break
        else:
            categories[f"Words without '{letter}'"].append(word)

    return categories

def get_mystery_word():
     return 'something'



miss = 0
number_of_guesses = 8
guessed_letters = []
mystery_word = get_mystery_word()    
display_word = '_________'



while miss < number_of_guesses:
        print('')
        print("Guessed Letters: " + ", ".join(guessed_letters))
        user_guess = input('Take a guess (1 letter): ').lower()
        

        if is_valid_guess(user_guess):
            guessed_letters.append(user_guess)
            build_word = ''

            for j in range(len(mystery_word)):

                if mystery_word[j] == user_guess:
                    build_word += mystery_word[j]
                else:
                    build_word += display_word[j]
            
            if user_guess not in mystery_word:
                miss += 1
                print(f'Swing and a miss. Guesses left: {number_of_guesses-miss}')
            else:
                print(f'Great guess! Misses: {number_of_guesses-miss}')
            
            print('---------------------------------------------')
            display_word = build_word
            print(display_word)
            print('')