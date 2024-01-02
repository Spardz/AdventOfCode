import json
import re


class Advent(object):
    def __init__(self):
        self.__win = {}
        self.__cards_won = {}
        self.__total_cards = {}

    def card_correct(self, entry):
        card = re.split(r'Card +', entry.split(':')[0].strip())[1]
        nums = re.split(r' +', entry.split(':')[1].strip().split('|')[0].strip())
        winning_nums = re.split(r' +', entry.split(':')[1].strip().split('|')[1].strip())

        self.__total_cards[card] = 1

        print(nums)
        print(winning_nums)

        self.__win[card] = {}
        correct_nums = 0
        for number in nums:
            if number in winning_nums:
                print(f'{number} found in winning nums.')
                self.__win[card][number] = True
                correct_nums = correct_nums + 1

        self.__cards_won[card] = correct_nums
        return correct_nums

    def execute(self, data):
        points = 0

        for entry in data:
            correct = self.card_correct(entry)
            if correct > 0:
                points = points + pow(2, correct - 1)

        i = 1
        tot = 0
        for card in self.__cards_won:
            have_cards = self.__total_cards[card]
            won = self.__cards_won[card]
            print('%s + %s = %s' % (tot, have_cards, tot + have_cards))
            tot = tot + have_cards
            for j in range(1, won + 1):
                if i + j < len(data) + 1:
                    self.__total_cards['%s' % (i + j)] = self.__total_cards['%s' % (i + j)] + have_cards

            i = i + 1

        print(json.dumps(self.__cards_won, sort_keys=False, indent=4))
        print(json.dumps(self.__total_cards, sort_keys=False, indent=4))
        print(tot)


if __name__ == '__main__':
    data = []
    with open('day4.txt') as fh:
        for line in fh:
            data.append(line.strip())

    Advent.execute(data)
