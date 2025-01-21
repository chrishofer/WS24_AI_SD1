import random

def ratespiel():
    erg = random.randint(1, 100)
    guess = -1
    versuche = 0
    print("Errate meine Zahl")
    while erg != guess:
        guess = int(input())
        versuche += 1

        if guess < erg:
            print("Zu niedrig geraten")
        if guess > erg:
            print("Zu hoch geraten")

    print(f'Richtig geraten nach {versuche} Versuchen')

if __name__ == '__main__':
    ratespiel()