import random

def guess_user_number(x, y):
    infimo = x
    supremo = y
    feedback = ''

    while feedback != 'c':
        try:
            feedback = ''
            guess = random.randint(infimo, supremo)
            print(f"El número es {guess}?")

            while not (feedback == 'a' or feedback == 'b' or feedback == 'c'):
                feedback = input(f"A: El número es muy bajo\nB: El número es muy alto\nC: El número es correcto\nIndica A, B o C: ")

            if feedback == 'a':
                infimo = guess + 1
            elif feedback == 'b':
                supremo = guess - 1
            elif feedback == 'c':
                print('Gané!')
        except ValueError:
            print('Ha ocurrido un error. Vuelve a intentarlo introduciendo correctamente los datos')
            break

    
    print('Fin')

        


guess_user_number(1, 100)