import re 

def read_input(path):
    return open(path, "r").read().strip().split("\n")

def solve1(input):
    lines = read_input(input)

    calibration = []
    for line in lines:
        matches = re.findall("\d", line)
        calibration.append(int(matches[0] + matches[-1]))

    return sum(calibration)

def solve2(input):
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    lines = read_input(input)

    reverse_numbers = [number[::-1] for number in numbers.keys()]

    calibration = []
    for line in lines:
        matches_left = re.findall(f"{'|'.join(numbers.keys())}|\d", line)
        matches_right = re.findall(f"{'|'.join(reverse_numbers)}|\d", line[::-1])

        calibration_left = numbers[matches_left[0]] if matches_left[0] in numbers.keys() else matches_left[0]

        calibration_right = numbers[matches_right[0][::-1]] if matches_right[0] in reverse_numbers else matches_right[0]

        calibration.append(int(f"{calibration_left}{calibration_right}"))
    
    return sum(calibration)


print(solve1("input"))
print(solve2("input"))