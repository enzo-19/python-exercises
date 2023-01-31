import random, sys, subprocess

elements = {
    'r': 'ROCK',
    'p': 'PAPER',
    's': 'SCISSORS'
}

# función que limpia la consola, no es imprescindible pero facilita la lectura del juego
def clear_screen():
    operating_system = sys.platform

    if operating_system == 'win32':
        subprocess.run('cls', shell=True)
    elif (operating_system == 'linux') or (operating_system == 'darwin'):
        subprocess.run('clear', shell=True)

def go_to_menu():
    action = ''

    while not (action == 's' or action == 'e'):
        print('"S" Start - "E" Exit')
        action = input("> ").lower()
        clear_screen()

    if action == 's':
        start_game()


def start_game():
    print('R for rock - P for paper - S for scissors')

    computer_choice = random.choice(list(elements.keys()))

    user_choice = input('> ')

    clear_screen()

    if not (user_choice == 'r' or user_choice == 'p' or user_choice == 's'):
        return go_to_menu()
    
    print(f"(you) {elements[user_choice]} vs. {elements[computer_choice]} (computer)")

    if (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
        print('You win')
    elif user_choice == computer_choice:
        print('Tie')
    else:
        print('You lose')

    return go_to_menu()


go_to_menu()