import random #import entire module

# from random import choice #imports only one/more function with , seperator
# from random import choice as ch #imports one/more funciton with your own name


# coin = random.choice(["heads","tails"])
# print(coin)
# ===========================
# number = random.randint(1, 100)
# print(number)
# ===============================

cards = ["king", "queen", "jack", "A",]
random.shuffle(cards)
for card in cards:
    print(card)

# print(type(cards))