import os


def syntax_error():
    path = os.getcwd()
    file_path = os.path.join(path, 'syntax.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    map = {")" : 3, "}": 1197, "]": 57, ">": 25137}
    score = 0
    score2 = []
    for line in Lines:
        input = line.strip()
        sequence = []
        corrupt = False
        for syntax in input:
            if syntax in ["(", "[", "{", "<"]:
                sequence.append(syntax)
            else:
                if len(sequence) != 0:   
                    curr = sequence.pop()
                if len(sequence) == 0 or not match(curr, syntax):
                    score += map.get(syntax)
                    corrupt = True
                    break
        if not corrupt:
            score2.append(complete_sequence(sequence))
    score2 = sorted(score2)
    print(score)
    print(score2[int(len(score2)/2)])


def match(open, close):
    if open == "(" and close == ")":
        return True
    if open == "[" and close == "]":
        return True
    if open == "{" and close == "}":
        return True
    if open == "<" and close == ">":
        return True
    return False

def complete_sequence(sequence):
    score = 0
    open_close = {"(" : ")", "{": "}", "[": "]", "<": ">"}
    map = {")" : 1, "}": 3, "]": 2, ">": 4}

    for brace in sequence[::-1]:
        score = score * 5
        score += map.get(open_close.get(brace))
    
    return score

    
if __name__ == "__main__":
    syntax_error()
