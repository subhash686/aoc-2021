import os

def power_consumption():
    path = os.getcwd()
    file_path = os.path.join(path, 'diagnostic.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    
    bitarray = []
    totalsets = 0
    for line in Lines:
        bits = line.strip()
        bitpos = 0
        if len(bitarray) == 0:
            bitarray = [0] * len(bits)
        for bit in bits:
            bitarray[bitpos] += int(bit)
            bitpos += 1
        totalsets += 1

    gamma = 0
    epsilon = 0
    power = 0
    bitarray.reverse()
    for bit in bitarray:
        gamma += (1 if bit > totalsets/2 else 0) * (2**power)
        epsilon += (0 if bit > totalsets/2 else 1) * (2**power)
        power += 1

    print(gamma * epsilon)

class Node():
    def __init__(self,key):
        self.key=key
        self.zcount=0
        self.ocount=0
        self.zero=None
        self.one=None

def ptree():
    path = os.getcwd()
    file_path = os.path.join(path, 'diagnostic.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    
    root = Node(-1)

    for line in Lines:
        bits = line.strip()
        bitpos = 0
        curr = root
        blen = len(bits)
        for bit in bits:
            if curr.zero is None:
                curr.zero = Node(0)
            if curr.one is None:
                curr.one = Node(1)
            if int(bit) == 0:
                curr.zcount += 1
                curr = curr.zero
            else:
                curr.ocount +=1
                curr = curr.one
    o2 = o2_generator_rating(root, blen)
    co2 = co2_generator_rating(root, blen)
    print(o2)
    print(co2)
    print(o2 * co2)

def o2_generator_rating(root: Node, blen):
    curr = root
    o2 = [0] * blen
    pos = 0
    while curr.one:
        if (curr.zcount > curr.ocount or curr.ocount == 0) and curr.zcount != 0:
            o2[pos] = 0
            curr = curr.zero
        else:
            o2[pos] = 1
            curr = curr.one
        pos +=1
    
    return bin_to_int(o2)

def co2_generator_rating(root: Node, blen):
    curr = root
    co2 = [0] * blen
    pos = 0
    while curr.zero or curr.one:
        if (curr.ocount < curr.zcount or curr.zcount == 0) and curr.ocount != 0:
            co2[pos] = 1
            curr = curr.one
        else:
            co2[pos] = 0
            curr = curr.zero
        pos +=1
    
    return bin_to_int(co2)
    
def bin_to_int(bits):
    num = 0
    bits.reverse()
    power = 0
    for bit in bits:
        num += bit * (2**power)
        power += 1

    return num
    

if __name__ == "__main__":
    power_consumption()
    ptree()
