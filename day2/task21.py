import re

def sum_possible_games():
    possible_games = []
    sum_possible_games = 0
    file_path = "input21.txt"
    red_max = 12
    green_max = 13
    blue_max = 14
    game_number_regex = "(\\d+(?=:))"
    sets_regex = "(?<=:)(.*)"
    red_regex = "(\\d+)(?=\\sred)"
    green_regex = "(\\d+)(?=\\sgreen)"
    blue_regex = "(\\d+)(?=\\sblue)"

    with open(file_path, "r") as file:
        for line in file:
            valid = True
            game_number = int(re.search(game_number_regex, line).group(0))
            sets = re.search(sets_regex, line).group(0)
            sets = re.split(";", sets)
            for game_set in sets:
                count_red = re.search(red_regex, game_set)
                if count_red:
                    count_red = int(count_red.group(0))
                    if count_red > red_max:
                        valid = False

                count_green = re.search(green_regex, game_set)
                if count_green:
                    count_green = int(count_green.group(0))
                    if count_green > green_max:
                        valid = False

                count_blue = re.search(blue_regex, game_set)
                if count_blue:
                    count_blue = int(count_blue.group(0))
                    if count_blue > blue_max:
                        valid = False

            if valid:
                possible_games.append(game_number)
                sum_possible_games += game_number

    print("Possible games number:", possible_games)
    print("Sum of possible games numbers:", sum_possible_games)

sum_possible_games()
