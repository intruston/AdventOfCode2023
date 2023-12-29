lottery_cards = open('input41.txt', 'r').readlines()
def calculate_points(cards):
    total_points = 0

    for card in cards:
        winning_numbers, card_numbers = map(str.split, card.split('|'))
        winning_set = set(winning_numbers)
        card_set = set(card_numbers)

        matches = len(winning_set.intersection(card_set))
        points = 2 ** (matches - 1) if matches > 0 else 0
        total_points += points

    return total_points

result = calculate_points(lottery_cards)
print("Total points:", result)
