import os

def count_increments():
    path = os.getcwd()
    file_path = os.path.join(path, 'sonar_sweep.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    
    prev = 0
    count = 0
    for line in Lines:
        current = int(line.strip())
        if current > prev:
            count = count +1
        prev = current

    print(count-1)

def count_increments_3sum():
    path = os.getcwd()
    file_path = os.path.join(path, 'sonar_sweep.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    
    prev = 0
    count = 0
    m = []
    lc = 0
    current = 0
    for line in Lines:
        lc = lc+1
        num = int(line.strip())
        current = current + num
        if lc < 4:
            m.append(num)
            prev = current
            continue
        else:
            current = current - m[0]
            m[0] = m[1]
            m[1] = m[2]
            m[2] = num
        if current > prev:
            count = count +1
        prev = current

    print(count)

if __name__ == "__main__":
    count_increments()
    count_increments_3sum()