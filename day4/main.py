
file = open("input", "r").read().strip().split("\n")

res = 0
for card in file:
    winning_numbers, my_numbers = card.split("|")
    winning_numbers = winning_numbers.split(":")[1].strip().split(" ")
    my_numbers = my_numbers.strip().split(" ")

    points = 0
    for number in my_numbers:
        for win in winning_numbers:
            if number == win and number != "":
                if points == 0:
                    points += 1
                else:
                    points *= 2

    res += points

print(res)



