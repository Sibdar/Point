from random import shuffle
from deck import Deck

class Hand:

    def __init__(self):
        # * Набор карт на руках у одного из игроков.
        self.cards = []

    # * Можно брать карты из колоды и добавлять "на руки".
    #   Метод `add_card` принимает объект `Card`.
    def add_card(self, deck):
        self.cards.append(deck.deal_card())

    # * После окончания игры можно убрать все карты (очистить `list`).
    def return_all_cards(self, deck):
        for n in range(len(self.cards)):
            deck.cards.append(self.cards.pop())

    # * Можно посчитать сумму очков (помним про туза).
    def count_points(self):
        _sum = sum(card.card_value() for card in self.cards)
        if 'A' in self.get_ranks() and _sum <= 21:
            return _sum + 10
        else:
            return _sum

    #  * Для удобства переопределить метод `__str__`, который возвращает строку со всеми
    #    картами "на руках" и их суммой (`count_points`).
    def __str__(self):
        return ', '.join([str(card) for card in self.cards]) + f' | {self.count_points()} оч.'

    def show_cards(self):
        print([card.card_value() for card in self.cards])

    def get_ranks(self):
        return [card.rank for card in self.cards]


def main():
    deck = Deck()
    hand = Hand()
    hand.add_card(deck)
    hand.add_card(deck)
    print(hand.get_ranks())
    hand.show_cards()
    print(hand.count_points())
    print(hand)


if __name__ == '__main__':
    main()


