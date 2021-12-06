import os

class Card:
    def __init__(self, id):
        self.id = id
        self.map = {}
        self.row_match = [0] * 5
        self.col_match = [0] * 5
        self.score = 0

def bingo_winning_board_score(win: bool):
    path = os.getcwd()
    file_path = os.path.join(path, 'bingo.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    
    line_num = 1
    id = 1
    row = 0
    col = 0
    cards = []
    card = None
    for line in Lines:
        input = line.strip()
        if line_num == 1:
            draws = input.split(",")
            line_num +=1
            continue
        if input == "":
            if card:
                cards.append(card)
            card = Card(id)
            id +=1
            row = 0
            continue
        else:
            cols = input.split(" ")
            col = 0
            for num in cols:
                if num == "":
                    continue
                card.map[num] = [row, col]
                card.score += int(num)
                col += 1
            row += 1
    if card:
        cards.append(card)
    if win:
        prev_pos = 10000
    else:
        prev_pos = -1
    final_score = 0
    final_card = 0
    for card in cards:
        pos = play_card(card, draws)
        if (win and pos < prev_pos) or (not win and pos > prev_pos):
            final_score = card.score * int(draws[pos])
            final_card = card.id
            prev_pos = pos

    print(final_card, prev_pos, final_score)

def play_card(card: Card, draws: list):
    pos = -1
    for draw in draws:
        pos += 1
        if card.map.get(draw, None):
            cell = card.map.get(draw)
            row = cell[0]
            col = cell[1]
            card.row_match[row] += 1
            card.col_match[col] += 1
            card.score -= int(draw)
            if card.row_match[row] == 5 or card.col_match[col] == 5:
                return pos


if __name__ == "__main__":
    bingo_winning_board_score(True)
    bingo_winning_board_score(False)
