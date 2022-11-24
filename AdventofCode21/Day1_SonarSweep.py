my_input = [int(line.strip()) for line in open("Day1_input.txt").readlines()]


def find_increases(depths):
    increases = 0
    for index, value in enumerate(depths):
        if value > depths[index-1]:
            increases += 1
    return increases


def find_increases_sums_of_three(depths):
    increases = 0
    for index, value in enumerate(depths):
        if (index != 0) and index < (len(depths)-2):
            if depths[index+2] > depths[index - 1]:
                increases += 1
    return increases


if __name__ == "__main__":
    print(find_increases_sums_of_three(my_input))