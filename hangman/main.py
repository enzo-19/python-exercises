from words import words
import string, random, sys, subprocess


# clear screen function
def clear_screen():
    operating_system = sys.platform

    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    elif (operating_system == 'linux') or (operating_system == 'darwin'):
        subprocess.run('clear', shell=True)

# get word from words.py file
def get_valid_word(words):
    word = random.choice(words)

    # buscamos una palabra formada exclusivamente por caracteres alfabéticos y que tenga al menos 5 letras
    while not word.isalpha() or len(word) < 5:
        word = random.choice(words)

    return word

def hangman():
    word_to_guess = get_valid_word(words).upper()
    lives = 6

    letters_to_guess = set(word_to_guess)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(letters_to_guess) > 0 and lives > 0:
        word_to_show = ''
        for letter in word_to_guess:
            if letter in letters_to_guess:
                word_to_show += '_ '
            else:
                word_to_show += letter + ' '
        print(f"Palabra: {word_to_show}")
        print(f"Letras usadas:", *used_letters)
        print(f"TIenes {lives} vidas")

        user_letter = input('Ingresa una letra: ').upper()

        clear_screen()

        if user_letter in (alphabet - used_letters):
            used_letters.add(user_letter)

            if user_letter in word_to_guess:
                letters_to_guess.remove(user_letter)
            else:
                print(f"La palabra no contiene '{user_letter}'")
                lives -= 1
        elif user_letter in used_letters:
            print(f"Ya has elegido '{user_letter}', intenta con otra letra.")
        else:
            print('El caracter ingresado no es válido')

    if lives > 0:
        print('Has ganado!')
    else:
        print('Has perdido!')
    print(f"La palabra a adivinar era: {word_to_guess}")

    


hangman()