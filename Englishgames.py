import random
import time

def home():
    print("1) Ita - Eng Animal Words! ")
    selection = int(input("What do you select? "))
    if selection==1: 
        game1()

def game1():
    player = input("What's your name? ")
    points = 0
    correct = 0
    streak = 0
    print("\nTry to translate 10 italian words now!")
    time.sleep(0.5)
    print("The game will start in 2 seconds!")
    time.sleep(2)
    print("Let's go!")
    
    for i in range(10):
        rand_num = random.randint(0, len(diz_ita_words))
        answer = input(f"Translate {diz_ita_words[rand_num]} : ")
        if answer == diz_eng_words[rand_num]:
            correct += 1
            streak += 1
            points += 2 + streak
            print(f"CORRECT! Your total points are: {points} and {streak} streak!")
        else:
            if streak > 0:
                streak = 0
                points -= 3
                print(f"WRONG! Your total points are: {points} . Streak lost.")
            else: 
                streak = 0
                points -= 2
                print(f"WRONG! Your total points are: {points} ")
            
            
    print("\nThe game is over! Here are your results!")
    print(f"*** {player} - {points} points! ***")
    print(f"You got {correct} correct answers out {i+1} , with a streak of {streak}")
    
    selection = int(input("\nDigit 1 to restart: "))
    if selection==1: 
        home()
    

#----------------------------
diz_ita_words = {
    0: "mucca",
    1: "serpente",
    2: "cavallo",
    3: "uccello", 
    4: "scimmia",
    5: "delfino",
    6: "giraffa",
    7: "pappagallo",
    8: "tigre",
    9: "leone",
    10: "cane",
    11: "gatto",
    12: "topo",
    13: "farfalla",
    14: "formica",
    15: "elefante",
    16: "puma",
    17: "dinosauro",
    18: "canguro",
    19: "lucertola",
    20: "pesce",
    21: "orso"
}    
diz_eng_words = {
    0: "cow",
    1: "snake",
    2: "horse",
    3: "bird",
    4: "monkey",
    5: "dolphin",
    6: "giraffe",
    7: "parrot",
    8: "tiger",
    9: "lion",
    10: "dog",
    11: "cat",
    12: "mouse",
    13: "butterfly",
    14: "ant",
    15: "elephant",
    16: "puma",
    17: "dinosaur",
    18: "kangaroo",
    19: "lizard",
    20: "fish",
    22: "bear"
}


home()


