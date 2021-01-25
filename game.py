from random import shuffle
from time import sleep
from deck import Deck
from player import Player


class Game:
    deck = Deck()
    counter = 0

    def __init__(self):
        Game.counter += 1

    def pause_game(self):
        suit_emojies = '\U00002660\U00002663\U00002665\U00002666'
        for suit in suit_emojies:
            print('  ' + suit, end=' ')
            sleep(0.75)
        # to next line
        print()

    # def start_new_game(self, *names):
    def start_new_game(self):
        print(f'> Добрый день! Сейчас сыграем в "Очко" (21).')
        self.pause_game()
        names = input('> Введите имена участников (через `, `): ').split(', ')
        self.players = [Player(name) for name in names]
        self.pause_game()
        print(f'> Игроки:\n' + ''.join([f'    {n + 1}) {player.name}.' for n, player in enumerate(self.players)]))
        self.pause_game()
        for player in self.players:
            player.add_card(Game.deck)
        print(f'> Каждый игрок получает по одной карте:\n' + ''.join(
            [f'    {n + 1}) {str(player)}' for n, player in enumerate(self.players)]))

    def play(self):
        shuffle(self.players)
        for player in self.players:
            self.pause_game()
            print(f'> Играет {player.name}.')
            while player.count_points() < 21:
                print(f'\t{str(player.hand)}')
                questions = ['Продолжаем?', 'Ещё?', 'Го?', 'Возьмешь ещё?', 'Рискнёшь взять ещё?']
                shuffle(questions)
                ans = input(f"  * {questions[0]} (y/n) ")
                if ans == 'y':
                    player.add_card(Game.deck)
                    if player.count_points() == 21:
                        player.is_winner = True
                        print(f'\t{str(player.hand)}')
                        answers = ['Кажется, ты вин!', 'Это твой день11!!!', f'{player.name}, да ты счастливчик!']
                        shuffle(answers)
                        print('  * ' + answers[0])
                    elif player.count_points() > 21:
                        player.is_winner = False
                        print(f'\t{str(player.hand)}')
                        answers = ['Кажется, перебор...', 'Немного пережали :)', 'В другой раз повезёт больше! :)']
                        shuffle(answers)
                        print('  * ' + answers[0])
                else:
                    print('> Закончили.')
                    break
            self.pause_game()
            print(f'> Итак, игрок {player.name} набрал {player.count_points()} оч.')
        # compare points
        self.pause_game()
        self.players.sort(key=lambda player: player.count_points())
        print('> Результаты:\n' + ''.join(
            [f'    {n + 1}) {player.name}: {player.count_points()} оч.' for n, player in enumerate(self.players)]))
        self.pause_game()
        print('> Выявляем победителя...')
        self.pause_game()
        winners = list(filter(lambda player: player.is_winner is True, self.players))
        below_21 = list(filter(lambda player: player.is_winner is None, self.players))
        above_21 = list(filter(lambda player: player.is_winner is False, self.players))
        print('> Победитель:')
        if winners:
            print('\t\U0001F3C6 ' + "".join([f"\t {winner.name}" for winner in winners]))
        elif below_21:
            print('\t\U0001F3C6 ' + str(below_21[-1].name))
        else:
            print('\t\U0001F3C6 ' + str(above_21[0].name))


def main():
    pass

if __name__ == '__main__':
    main()