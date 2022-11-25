from collections import Counter

my_input = [line.strip() for line in open("Day3_input.txt").readlines()]


def calc_power_consumption(diagnostic_report):
    bits = len(diagnostic_report[0])  # each line in diagnostic_report is a bit-string made of 12 bits
    my_array = ['']*bits  # create empty array for collecting data bit-wise
    for bit in range(bits):
        for bitstring in diagnostic_report:
            my_array[bit] += bitstring[bit]
    gamma, epsilon = '', ''
    for i, bit_list in enumerate(my_array):
        occurrence = Counter(bit_list)
        gamma += occurrence.most_common()[0][0]
        epsilon += occurrence.most_common()[-1][0]
    gamma, epsilon = int(gamma, 2), int(epsilon, 2)
    power_consumption = gamma * epsilon
    return power_consumption


if __name__ == "__main__":
    print(calc_power_consumption(my_input))