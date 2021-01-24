class Card:
    # rank - название карты, suit - масть
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        # return " AJQK 6789t".index(self.rank)
        return [None, 'A', 'J', 'Q', 'K', None, '6', '7',
                '8', '9', '10', 'A'].index(self.rank)

# * Для удобства переопределить метод `__str__`, который
#   возвращает строку с `rank` и `suit`.
    def __str__(self):
        return f'{self.rank} {self.suit}'


def main():
    card = Card('A', 'Пики')
    print(card.card_value())
    print(card)


if __name__ == '__main__':
    main()





