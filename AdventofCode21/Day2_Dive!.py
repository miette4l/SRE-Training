my_input = [(line.strip().split()) for line in open("Day2_input.txt").readlines()]
co_ords = (0, 0)


def calculate_positions(initial_co_ords, course):
    (h, d) = initial_co_ords
    for line in my_input:
        if line[0] == "forward":
            h += int(line[1])
        elif line[0] == "down":
            d += int(line[1])
        elif line[0] == "up":
            d -= int(line[1])
    return h*d


if __name__ == "__main__":
    print(calculate_positions(co_ords, my_input))