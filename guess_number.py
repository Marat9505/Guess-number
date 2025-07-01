import random

def random_number():
    return random.randint(1, 100)

def play_game():
    secret = random_number()
    attempts = 0
    print("Փորձեք գուշակել թիվը 1-ից 100 միջակայքում։")

    while True:
        try:
            guess = int(input("Խնդրում եմ մուտքագրեք թիվ: "))
            attempts += 1

            if guess == secret:
                print(f"🎉 Շնորհավորում եմ, դուք հաղթեցիք {attempts} փորձից հետո!")
                break
            elif guess > secret:
                print(f"Ձեր թիվը շատ մեծ է։ Փորձ N°{attempts}")
            else:
                print(f"Ձեր թիվը փոքր է։ Փորձ N°{attempts}")
        except ValueError:
            print("⚠️ Խնդրում եմ մուտքագրեք միայն ամբողջ թիվ։")

play_game()
