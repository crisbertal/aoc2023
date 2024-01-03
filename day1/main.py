import re 


def read_input(path):
    return open(path, "r").read().strip().split("\n")


def calibrate(lines):
    calibration = []
    for line in lines:
        matches = re.findall("\d", line)
        calibration.append(int(matches[0] + matches[-1]))

    return sum(calibration)


def solve1(input):
    lines = read_input(input)
    return calibrate(lines)


def solve2(input):
    lines = read_input(input)

    new_lines = []
    for line in lines:
        line = line.replace("one", "o1ne")
        line = line.replace("two", "t2wo")
        line = line.replace("three", "t3hree")
        line = line.replace("four", "f4our")
        line = line.replace("five", "f5ive")
        line = line.replace("six", "s6ix")
        line = line.replace("seven", "s7even")
        line = line.replace("eight", "e8ight")
        line = line.replace("nine", "n9ine")
        new_lines.append(line)

    return calibrate(new_lines)


print(solve1("input"))
print(solve2("input"))