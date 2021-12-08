import os


def count_digits(easy):
    path = os.getcwd()
    file_path = os.path.join(path, 'seg_search.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    count = 0
    out = 0
    for line in Lines:
        input = line.strip()
        io = input.split("|")
        output = io[1].strip().split(" ")
        power = 3
        map = {}
        for digit in output:
            length = len(digit)
            if length in [2,3,4,7]:
                count += 1
            else:
                if len(map) == 0:
                    map = decode(io[0].strip())

            num = find(digit, map)
            out += num * (10 ** power)
            power -=1

    print(count)
    print(out)


def decode(digits):
    map = {"a":"0", "b": "0", "c": "0", "d" : "0", "e" : "0", "f": "0", "g":"0"}
    countmap = {x : [] for x in range(2,8)}
    for digit in digits.split(" "):
        length = len(digit)
        countmap[length].append(digit)

    one = countmap.get(2)[0]
    four = countmap.get(4)[0] 
    seven = countmap.get(3)[0]
    six = ""
    zero = ""
    for char in one:
        for digit in countmap.get(6):
            if char not in digit:
                map["c"] = char
                six = digit
                break
        if six != "":
            break
    for char in six:
        for digit in countmap.get(6):
            if digit == six:
                continue
            if char not in digit:
                if char in four:
                    map["d"] = char
                    zero = digit
                else:
                    map["e"] = char
                    nine = digit
            if map["d"] != "0" and map["e"] != "0":
                break

    for char in zero:
        if char in four and char not in seven:
            map["b"] = char

    return map


def find(digit, map):
    length = len(digit)
    num = 0
    if length == 2:
        num = 1
    elif length == 3:
        num = 7
    elif length == 4:
        num  = 4
    elif length == 7:
        num = 8
    elif length == 6:
        if map["c"] not in digit:
            num = 6
        elif map["d"] not in digit:
            num = 0
        elif map["e"] not in digit:
            num = 9
    elif length == 5 and map:
        if map["e"] in digit:
            num = 2
        elif map["b"] in digit:
            num = 5
        elif map["b"] not in digit and map["e"] not in digit:
            num = 3        
    
    return num

if __name__ == "__main__":
    count_digits(True)
