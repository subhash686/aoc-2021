import os


def align(step):
    path = os.getcwd()
    file_path = os.path.join(path, 'whales.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    initial_pos = [0] * 2000
    final = 0
    for line in Lines:
        input = line.strip()
        poss = input.split(",")
        prev_fuel = -1
        for median in range(0, int(poss[len(poss)-1])+1):
            fuel = 0
            for pos in poss:
                n = abs(int(pos) - int(median))
                fuel += n * (n+1)/2 if step else n
            if fuel < prev_fuel or prev_fuel == -1:
                prev_fuel = fuel

    print(int(prev_fuel))


if __name__ == "__main__":
    align(False)
    align(True)
