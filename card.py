import random

CARD_MAPPER = {
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': '10',
    '11': 'J',
    '12': 'Q',
    '13': 'K',
    '14': 'A'    
}

COLOR_MAPPER = {
    '0': 'a',
    '1': 'b',
    '2': 'c',
    '3': 'd'
}

class Card:
    def __init__(self, color, figure):
        self.color = color
        self.figure = figure

    def __str__(self):
        return f"Color: {self.color}, Figure: {self.figure}"

class Deck:
    def __init__(self, number_of_cards):
        self.number_of_cards = number_of_cards
        self.list_of_cards = self.generate_deck()

    def add_card(self, added_card):
        self.list_of_cards.append(added_card)

    def generate_deck(self):
        all_cards = []
        for card in range(self.number_of_cards):
            all_cards.append(Card(random.randint(0, 3), random.randint(2, 14)))
        return all_cards

    def get_deck(self):
        return self.list_of_cards

    def pass_random_card(self):
        rand_card = random.randint(0, self.number_of_cards - 1)
        tmp_card = self.get_deck()[rand_card]
        self.number_of_cards -= 1
        del self.list_of_cards[rand_card]
        return tmp_card

class Player:
    def __init__(self, name, surname, gender, number_of_player_cards = 24):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.player_deck = Deck(number_of_player_cards)
        self.points = 0

    def __str__(self):
        return f'Name: {self.name} {self.surname}, Gender: {self.gender}'

class Game:
    def __init__(self, names, surnames, genders, n_of_cards = [24, 24]):
        self.player_one = Player(names[0], surnames[0], genders[0], n_of_cards[0])
        self.player_two = Player(names[1], surnames[1], genders[1], n_of_cards[1])

    def gameplay(self):
        while self.player_one.player_deck.number_of_cards > 0 and self.player_two.player_deck.number_of_cards > 0:
            card_1 = self.player_one.player_deck.pass_random_card()
            card_2 = self.player_two.player_deck.pass_random_card()
            if card_1.figure > card_2.figure:
                print(f'{CARD_MAPPER[str(card_1.figure)]} wygrywa nad {CARD_MAPPER[str(card_2.figure)]}')
                self.player_one.points += 1
            elif card_1.figure < card_2.figure:
                print(f'{CARD_MAPPER[str(card_1.figure)]} przegrywa z {CARD_MAPPER[str(card_2.figure)]}')
                self.player_two.points += 1
            else:
                print(f'{CARD_MAPPER[str(card_1.figure)]} remis z {CARD_MAPPER[str(card_2.figure)]}')
            print(f'Punkty gracza 1: {self.player_one.points}\nPunkty gracza 2: {self.player_two.points}')
###############################################

main_game = Game(["Jan", "Adam"], ["Nowak", "Kowalski"], ["M", "M"])
main_game.gameplay()