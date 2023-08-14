import random
from colorama import init, Fore, Back, Style

init()

def play_game():
    def draw_hangman(misses):
        hangman = [
            # 0 misses
            """
                
                    
                    
                    
                    
                    
                    
                    
            """,
            # 1 miss
            """
                
                    
                    
                    
                    
                    
                    
            ===========        
            """, 
            # 2 misses
            """
                +---+
                    |
                    |
                    |
                    |
                    |
                    |
            ===========        
            """,
            # 3 misses
            """
                +---+
                |   |
                O   |
                    |
                    |
                    |
                    |
            ===========        
            """,
            # 4 misses
            """
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                    |
            ===========        
            """, 
            # 5 misses
            """
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
                    |
            ===========        
            """, 
            # 6 misses
            """
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
                    |
            ===========        
            """,
            # 7 misses
            """
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
                    |
            ===========        
            """, 
            # 8 misses
            """
                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
                    |
            ===========        
            """

        ]
        bright_hangman = [Style.BRIGHT + man + Style.RESET_ALL for man in hangman]
        return bright_hangman[misses]

    
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
        
    def choose_difficulty():
        prompt = """
    Choose difficulty:
    e - Easy
    m - Medium
    h - Hard
    """
        print(prompt)

        difficulty = input("Enter your choice: ").lower()

        if difficulty == 'e':
            return 'easy'
        elif difficulty == 'm':
            return 'medium'
        elif difficulty == 'h':
            return 'hard'
        else:
            print('Invalid choice. Please choose a valid difficulty.')
            return choose_difficulty()

    def get_mystery_word(difficulty_level):
        mystery_word = random.choice(lines).strip()
        if difficulty_level == 'easy':
            if 4 <= len(mystery_word) <= 6:
                return mystery_word
            else:
                return get_mystery_word('easy')
        elif difficulty_level == 'medium':
            if 6 <= len(mystery_word) <= 8:
                return mystery_word
            else:
                return get_mystery_word('medium')
        elif difficulty_level == 'hard':
            if 8 <= len(mystery_word):
                return mystery_word
            else:  
                return get_mystery_word('hard')

    def restart_game():

        user_yes_or_no = input('Want to play again [y/n]?: ')

        if user_yes_or_no == 'y':
            # Restart Game
            play_game()
        elif user_yes_or_no == 'n':
            print('')
            print('Good playing! See you next time.')
            return # need return statement to end game. 
        else:
            print('Invalid choice. Please enter "y" or "n" to play again')
            return restart_game()

    # get words from text file
    file_path = "words.txt"  

    # Open the file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # initialize game
    miss = 0
    number_of_guesses = 8
    guessed_letters = []
    
    # def initialize_game():
    #     choose_difficulty()
    #     get_mystery_word()
    #     display_starting_menu()

    # Introduction Text
    print('')
    print(Fore.RED + Style.BRIGHT + "Welcome to Hangman!" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Guess the letters to save the hangman!" + Style.RESET_ALL)

    difficulty_level = choose_difficulty()
    print(f"You chose {difficulty_level} difficulty.")

    # Choose a word randomly (one word on each line)
    mystery_word = get_mystery_word(difficulty_level)
    
    display_word = '_______________________________'

    # display start
    print('')
    print(f'The secret word contains {len(mystery_word)} letters')

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
            print(draw_hangman(miss))
            print(display_word)
            print('')

            if display_word == mystery_word:
                print(f'You got it! Misses: {miss}')
                restart_game()
                return # exit the game loop 

            if miss == number_of_guesses:
                dead_prompt = f"""
    You Dead.            
    The word was {mystery_word}                        
    """     
                print(dead_prompt)
                restart_game()
                return # exit the game loop 


if __name__ == "__main__":
    play_game()
