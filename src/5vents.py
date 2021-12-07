import os

plane = [[0 for i in range(1000)] for j in range(1000)]

count = [0]


def overlapping_vents():
    path = os.getcwd()
    file_path = os.path.join(path, 'vents.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    for line in Lines:
        input = line.strip()
        points = input.split(" -> ")
        plot(points[0], points[1])

    print(count[0])

def plot(point1, point2):
    p1 = point1.split(",")
    p2 = point2.split(",")
    x1 = int(p1[0])
    x2 = int(p2[0])
    y1 = int(p1[1])
    y2 = int(p2[1])

    if x1 == x2 and y1 == y2:
        addpoints(x1, y1)
    elif x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2+1):
            addpoints(x1, y)
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2+1):
            addpoints(x, y1)
    else:
        slope = (y2-y1)/ (x2-x1)
        intercept = y1 - (x1 * slope)
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2+1):
            addpoints(x, int(x*slope)+int(intercept))

def addpoints(x, y):
    if plane[x][y] == 1:
        count[0] +=1
    plane[x][y] += 1

if __name__ == "__main__":
    overlapping_vents()
