from deck import Deck
from hand import Hand

class Player:
    def __init__(self, name):
        # * Есть имя. Принимает его в конструкторе.
        self.name = name
        # * Есть рука и в ней карты (пустой объект `Hand`).
        self.hand = Hand()
        self.is_winner = None

    # * Может добавить в руку карту (переданну как аргумент).
    def add_card(self, deck):
        return self.hand.add_card(deck)

    # * После окончания игры можно убрать все карты
    def clear_cards(self, deck):
        return self.hand.return_all_cards(deck)

    def count_points(self):
        return self.hand.count_points()

    def __str__(self):
        return f'{self.name}: ' + str(self.hand)



def main():
    deck = Deck()
    player = Player('Ilia')
    player.add_card(deck)
    player.add_card(deck)
    print(player)


if __name__ == '__main__':
    main()