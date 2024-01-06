
file = open("input", "r").read().strip().split("\n")

GRID = [[symbol for symbol in line] for line in file]
ROWS = len(GRID)
COLS = len(GRID[0])
VALUES = "0123456789."

def solve1():
    gears = []
    for row in range(ROWS):
        n = 0
        has_part = False
        # COLS + 1 to get numbers in the edge
        for col in range(COLS + 1):
            if col < COLS and GRID[row][col].isdigit():
                n = n * 10 + int(GRID[row][col])
                for row_dir in [-1, 0, 1]:
                    for col_dir in [-1, 0, 1]:
                        if 0 <= row + row_dir < ROWS and 0 <= col + col_dir < COLS:
                            symbol = GRID[row + row_dir][col + col_dir] 
                            if symbol not in VALUES:
                               has_part = True
            else:
                if has_part:
                    gears.append(n)
                    has_part = False
                n = 0

    return sum(gears)

def solve2():
    # multiply common symbol position
    gear_symbol_values = {}
    res = 0
    for row in range(ROWS):
        n = 0
        has_part = False
        gear_position = []
        for col in range(COLS + 1):
            if col < COLS and GRID[row][col].isdigit():
                n = n * 10 + int(GRID[row][col])
                for row_dir in [-1, 0, 1]:
                    for col_dir in [-1, 0, 1]:
                        if 0 <= row + row_dir < ROWS and 0 <= col + col_dir < COLS:
                            symbol = GRID[row + row_dir][col + col_dir] 
                            if symbol not in VALUES and symbol == "*":
                                gear_position = (row + row_dir, col + col_dir)
                                has_part = True

            else:
                if has_part:
                    if len(gear_symbol_values) == 0 or gear_position not in gear_symbol_values.keys():
                        gear_symbol_values[gear_position] = [n]
                    else:
                        gear_symbol_values[gear_position].append(n)
                    has_part = False
                    gear_position = []
                    print(gear_symbol_values)
                n = 0

    for _, values in gear_symbol_values.items():
        mul = 1
        if len(values) > 1:
            for value in values:
                mul *= value
            res += mul

    return res



print(solve1())
print(solve2())
