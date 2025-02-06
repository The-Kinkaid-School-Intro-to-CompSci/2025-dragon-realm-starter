import random
import time

game_playing = "yes"
while game_playing == "yes" or game_playing == "y":
    print("Welcome to the Dragon Realm!\n")
    print(''' You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly and will
share his treasure with you. The other dragon is greedy and hungry,
and will eat you on sight!''')
    print("Choose wisely!")

    # choosing a cave
    chosen_cave = ''
    while chosen_cave != '1' and chosen_cave != '2':
        chosen_cave = input("What cave will you go in to, 1 or 2? ")
    #cave chosen--more action
    print("Slowly, you approach the cave...")
    time.sleep(1)
    print("It's dark and spooky...")
    time.sleep(1)
    print("A large dragon jumps out in front of you!")
    print("He opens his jaws and...")
    time.sleep(1)
    #choose a cave randomly to be the "good cave"
    good_cave = random.randint(1,2)
    if good_cave == int(chosen_cave):
        print("He gives you a big hug and his treasure!")
    else:
        print("He eats you in one bite!")
    
    #resetting the game
    game_playing = input("Would you like to play again? yes / no ")
