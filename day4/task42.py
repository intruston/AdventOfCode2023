lottery_cards = open('input41.txt', 'r').readlines()
def calculate_combinations(cards):
    total_combinations = [1] * len(cards)

    for i, card in enumerate(cards):
        winning_numbers, card_numbers = map(str.split, card.split('|'))
        matches = len(set(winning_numbers) & set(card_numbers))

        for j in range(i + 1, min(i + 1 + matches, len(cards))):
            total_combinations[j] += total_combinations[i]

    return sum(total_combinations)

result = calculate_combinations(lottery_cards)
print("Total combinations:", result)

