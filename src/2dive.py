import os

def final_cartisan_coordinate():
    path = os.getcwd()
    file_path = os.path.join(path, 'dive.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    
    X = 0
    Z = 0
    for line in Lines:
        direction = line.strip()
        nav = direction.split(" ")
        measure = int(nav[1])
        if nav[0] == "forward":
            X = X + measure
        elif nav[0] == "up":
            Z = Z - measure
        elif nav[0] == "down":
            Z = Z + measure

    print(X*Z)

def final_cartisan_coordinate_with_aim():
    path = os.getcwd()
    file_path = os.path.join(path, 'navigate.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    
    X = 0
    Z = 0
    A = 0
    for line in Lines:
        direction = line.strip()
        nav = direction.split(" ")
        measure = int(nav[1])
        if nav[0] == "forward":
            X = X + measure
            Z = Z + (A * measure)
        elif nav[0] == "up":
            A = A - measure
        elif nav[0] == "down":
            A = A + measure

    print(X*Z)

if __name__ == "__main__":
    final_cartisan_coordinate()
    final_cartisan_coordinate_with_aim()
