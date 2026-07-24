import random

cards = ["Ace", "King", "Queen", "Jack", "10"]
print(f"Original list: {cards}")

random.shuffle(cards)
print(f"Shuffled list: {cards}")