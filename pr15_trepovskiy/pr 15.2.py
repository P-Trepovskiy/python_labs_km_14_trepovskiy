def gen_card(card, suit):
    yield f'{card} {suit}'


suits = ['diamonds', 'clubs', 'hearts', 'spades']
num_cards = [i for i in range(2, 11)]
all_cards = ['A', 'J', 'Q', 'K']
for i in num_cards:
    all_cards.append(i)

for i in suits:
    for j in all_cards:
        card = gen_card(j, i)
        print(next(card))

raise StopIteration