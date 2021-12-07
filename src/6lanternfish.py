import os


def populate_fish(days):
    path = os.getcwd()
    file_path = os.path.join(path, 'lanternfish.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    initial_ages = [0] * 9
    final = 0
    for line in Lines:
        input = line.strip()
        ages = input.split(",")
        for age in ages:
            initial_ages[int(age)] += 1

    for day in range(1, days+1):
        reset = initial_ages[0]
        initial_ages[0] = 0
        for age in range(0, 8):
            initial_ages[age] = initial_ages[age+1]
        initial_ages[8] = 0
        initial_ages[6] += reset
        initial_ages[8] += reset

    for final_age in initial_ages:
        final += final_age

    print(final)


if __name__ == "__main__":
    populate_fish(80)
    populate_fish(256)
