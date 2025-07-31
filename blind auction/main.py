# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

bids = {}
again = "yes"
while again == "yes":

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    again = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if again == "yes":
        print("\n" * 20)

winner = ""
highest_bid = 0
for name in bids:
    if bids[name] >= highest_bid:
        highest_bid = bids[name]
        winner = name

print(f"The winner is {winner} with a bid of {highest_bid}")
