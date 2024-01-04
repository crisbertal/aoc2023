import re


def read_input(input):
    return open(input).read().strip().split("\n")


def solve1(input):
    file = read_input(input)
    valid_games = []
    for game in file:
        split_game = game.replace("Game ", "").split(":")
        id, rounds = split_game[0], split_game[1].split(";")
        not_valid = False
        for round in rounds:
            plays = round.split(",")
            for play in plays:
                count, color = play.strip().split(' ')
                count = int(count)
                if (color == "red" and count > 12) or (color == "green" and count > 13) or (color == "blue" and count > 14):
                    not_valid = True
                    break
            if not_valid:
                break
        if not not_valid:
            valid_games.append(int(id))


    return sum(valid_games)

def solve2(input):
    file = read_input(input)
    power = 0
    for game in file:
        max_blue = max([int(match.replace(" blue", "")) for match in re.findall("\d+[\s]blue", game)])
        max_red = max([int(match.replace(" red", "")) for match in re.findall("\d+[\s]red", game)])
        max_green = max([int(match.replace(" green", "")) for match in re.findall("\d+[\s]green", game)])
        power += max_blue * max_red * max_green
    return power

print(solve1("input"))
print(solve2("input"))
