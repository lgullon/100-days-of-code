import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ")

while play_again == 'y':
    print("\n" * 100)
    print(art.logo)
    player = list()
    computer = list()

    computer.append(random.choice(cards))
    computer.append(random.choice(cards))

    if sum(computer) == 21:
        c_blackjack = True
    else:
        c_blackjack = False

    while sum(computer) < 17:
        computer.append(random.choice(cards))
        if sum(computer) > 21 and 11 in computer:
            ace_index = computer.index(11)
            computer[ace_index] = 1

    player.append(random.choice(cards))
    player.append(random.choice(cards))

    if sum(player) == 21:
        p_blackjack = True
    else:
        p_blackjack  = False
    print(f"Your cards: {player}, current score: {sum(player)}")
    print(f"Computer's first card: {computer[0]}")

    draw = input("Type 'y' to get another card, type 'n' to pass: ")
    while draw == 'y':
        player.append(random.choice(cards))
        if sum(player) > 21 and 11 in player:
            ace_index = player.index(11)
            player[ace_index] = 1
        if sum(player) > 21:
            break
        print(f"Your cards: {player}, current score: {sum(player)}")
        print(f"Computer's first card: {computer[0]}")
        draw = input("Type 'y' to get another card, type 'n' to pass: ")



    p_total = sum(player)
    c_total = sum(computer)
    print(f"Your final hand: {player}, final score: {p_total}")
    print(f"Computer's final hand: {computer}, final score: {c_total}")


    if p_blackjack and c_blackjack:
        print("Wow! You both got BLACKJACKS! It's a tie!")
    elif p_blackjack:
        print("You got a BLACKJACK! You win!")
    elif c_blackjack:
        print("The computer got a BLACKJACK! You lose.")

    if p_total > 21 and c_total > 21:
        print(f"You both went over but you still lose :p")
    elif p_total > 21:
        print("You went over, you lose :(")
    elif c_total > 21:
        print("You win!!")
    else:
        if p_total > c_total:
            print("You win!!")
        elif p_total < c_total:
            print("You lose :(")
        else:
            print("It's a tie..")

    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ")
