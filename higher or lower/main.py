import random
import art
from game_data import data

print(art.logo)

def random_person(taken):
    '''Returns a random person from the game data, excluding the parameter "taken"'''
    person = taken
    while person == taken:
        person = data[random.randint(0, len(data) - 1)]
    return person

def more_followers(first, second, choice):
    '''Returns true if the chosen person has more followers, false otherwise.'''
    if choice == 'A':
        if first['follower_count'] >= second['follower_count']:
            return True
        else:
            return False
    else:
        if first['follower_count'] <= second['follower_count']:
            return True
        else:
            return False

# repeat until the player loses
correct = True
score = 0
last_person = random_person(None)
while correct:
    # choose person A
    person_A = last_person
    print(f"Compare A: {person_A['name']}, a {person_A['description']} from {person_A['country']}.")

    print(art.vs)

    # choose person B
    person_B = random_person(person_A)
    print(f"Against B: {person_B['name']}, a {person_B['description']} from {person_B['country']}.")
    last_person = person_B

    # get input
    guess = input("Who has more followers? Type 'A' or 'B':  ")

    # check input
    correct = more_followers(person_A, person_B, guess)
    print("\n" * 100)
    print(art.logo)
    if correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
