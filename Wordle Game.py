import random

def word_game():
    easy_bank = ["mice","dog","cat","hat","cake","bulb","ship","boat","sea","lake","sun","bag","bat","foot","boot","wall","ball","mat","cap","toe","bows","mow","cows","plow","eyes","fire","tire","car","mars","moon","cart","mart"]
    medium_bank = ["monkey","parrot","bannana","train","vacation","walmart","football","swimming","flower","seagull","plants","carpet","computer","blinds","pancake","gallery","school","charger","arbys","cloudy","rackets","blooming","working","bakery","oceans","walking","running","jumping"]
    hard_bank = ["capybaras","sunbathing","photosyntheisis","traveling","wolverine","militarys","chocalate","lightning","educational","brightness","landscapping","meditation","fragrance","reflection","exhaling","mcdonalds","investigate","participant","volunteers","helicopter","skateboard","telescope","microphone"]
    attempts = 1
    user_word = []

    print("Welcome to Word Guesser!")
    print("------------------------")
    print("* Press E for easy mode, M for meduim, and H for hard:",end= "")
    levels = ["e","m","h"]
    mode = input(" ").lower()

    if mode not in levels:
        print("\n***Make sure to press M, E, or H then enter next time!\n")
        word_game()

    if mode == "e":
        word = ""
        random_word = random.choice(easy_bank)

        print("Instructions:")
        print(" - In this game you will have 10 attempts to guess a letter or word")
        print(" - The word can be a place, thing, or animal")
        print(" - If a letter you guessed is in the word, it will be shown where in the word it is located")
        print(" - If you guess the word correct you win!")
        print(" - Enter any button to begin:",end = "")
        user_input = input(" ")
        print("---------------------------------------------------------------------------------------------------------------------- ")

        for nums in range(len(random_word)):
            user_word.append("_")

        while attempts < 11:
            print(f"Attempt {attempts}."," ".join(user_word)," Guess a letter or word:",end= "")
            user_guess = input(" ")
            attempts += 1

            if len(user_guess) == 1:
                for y in range(0,len(random_word)):
                    if user_guess == random_word[y]:
                        user_word[y] = user_guess
                if "".join(user_word) == random_word:
                    word = "".join(user_word)
                    print("\n------------------------------------------------")
                    print("Good job you won!!")
                    print("Word:",random_word)
                    break
                elif random_word != "".join(user_word) and attempts == 11:
                    break
            
            if "".join(user_word) == random_word:
                word = "".join(user_word)
                print("\n----------------------------------------------")
                print("Good job you won!!")
                print("Word:",random_word)
                break

            if len(user_guess) != 1 and len(user_guess) != len(random_word):
                print("***Make sure to enter one letter or the same amount of charecters as the word!")
                pass

            if len(user_guess) == len(random_word):
                if user_guess == random_word:
                    word = user_guess
                    print("\n---------------------------------------------------")
                    print("Good job you won!!")
                    print("Word:",random_word)
                    break

        if word != random_word:
            print("\n--------------------------------------------------")
            print("Better luck next time!")
            print("Word:",random_word)


    if mode =="m":
        word = ""
        random_word = random.choice(medium_bank)

        print("Instructions:")
        print(" - In this game you will have 10 attempts to guess a letter or word")
        print(" - The word can be a place, thing, or animal")
        print(" - If a letter you guessed is in the word, it will be shown where in the word it is located")
        print(" - If you guess the word correct you win!")
        print(" - Enter any button to begin:",end = "")
        user_input = input(" ")
        print("---------------------------------------------------------------------------------------------------------------------- ")

        for nums in range(len(random_word)):
            user_word.append("_")

        while attempts < 11:
            print(f"Attempt {attempts}."," ".join(user_word)," Guess a letter or word:",end= "")
            user_guess = input(" ")
            attempts += 1

            if len(user_guess) == 1:
                for y in range(0,len(random_word)):
                    if user_guess == random_word[y]:
                        user_word[y] = user_guess
                if "".join(user_word) == random_word:
                    word = "".join(user_word)
                    print("\n---------------------------------------------------")
                    print("Good job you won!!")
                    print("Word:",random_word)
                    break
                elif random_word != "".join(user_word) and attempts == 11:
                    break
            
            if "".join(user_word) == random_word:
                word = "".join(user_word)
                print("\n----------------------------------------------")
                print("Good job you won!!")
                print("Word:",random_word)
                break

            if len(user_guess) != 1 and len(user_guess) != len(random_word):
                print("***Make sure to enter one letter or the same amount of charecters as the word!")
                pass

            if len(user_guess) == len(random_word):
                if user_guess == random_word:
                    word = user_guess
                    print("\n---------------------------------------------------")
                    print("Good job you won!!")
                    print("Word:",random_word)
                    break

        if word != random_word:
            print("\n--------------------------------------------------------")
            print("Better luck next time!")
            print("Word:",random_word)


    if mode == "h":
        word = ""
        random_word = random.choice(hard_bank)

        print("Instructions:")
        print(" - In this game you will have 10 attempts to guess a letter or word")
        print(" - The word can be a place, thing, or animal")
        print(" - If a letter you guessed is in the word, it will be shown where in the word it is located")
        print(" - If you guess the word correct you win!")
        print(" - Enter any button to begin:",end = "")
        user_input = input(" ")
        print("---------------------------------------------------------------------------------------------------------------------- ")

        for nums in range(len(random_word)):
            user_word.append("_")

        while attempts < 11:
            print(f"Attempt {attempts}."," ".join(user_word)," Guess a letter or word:",end= "")
            user_guess = input(" ")
            attempts += 1

            if len(user_guess) == 1:
                for y in range(0,len(random_word)):
                    if user_guess == random_word[y]:
                        user_word[y] = user_guess
                if "".join(user_word) == random_word:
                    word = "".join(user_word)
                    print("\n------------------------------------------------")
                    print("Good job you won!!")
                    print("Word:",random_word)
                    break
                elif random_word != "".join(user_word) and attempts == 11:
                    break
            
            if "".join(user_word) == random_word:
                word = "".join(user_word)
                print("\n----------------------------------------------")
                print("Good job you won!!")
                print("Word:",random_word)
                break

            if len(user_guess) != 1 and len(user_guess) != len(random_word):
                print("***Make sure to enter one letter or the same amount of charecters as the word!")
                pass

            if len(user_guess) == len(random_word):
                if user_guess == random_word:
                    word = user_guess
                    print("\n---------------------------------------------------")
                    print("Good job you won!!")
                    print("Word:",random_word)
                    break

        if word != random_word:
            print("\n--------------------------------------------------------")
            print("Better luck next time!")
            print("Word:",random_word)
        

word_game()
