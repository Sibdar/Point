from random import shuffle
from card import Card

class Deck:
    # ranks = "AJQK6789t"
    ranks = ('A', 'J', 'Q', 'K', '6', '7', '8', '9', '10')
    # spade, club, heart, diamond
    suits = '\U00002660\U00002663\U00002665\U00002666'
    # suits = 'БПКЧ
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in Deck.ranks for suit in Deck.suits]
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


def main():
    deck = Deck()
    print([str(card) for card in deck.cards])
    print(len(deck.cards))


if __name__ == '__main__':
    main()




