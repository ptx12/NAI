from typing import List, Tuple
from collections import Counter
import sys
from lol import com, a

test_units = [

]

def build_codes(tree, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    _, content = tree
    if isinstance(content, str):
        codebook[content] = prefix
    else:
        left, right = content
        build_codes(left, prefix + "0", codebook)
        build_codes(right, prefix + "1", codebook)

    return codebook

def build_tree(forest):
    while len(forest) > 1:
        forest = sorted(forest, key=lambda x: x[0])
        left = forest.pop(0)
        right = forest.pop(0)

        forest.append((left[0] + right[0], (left, right)))

    return forest[0]


def huffman(input: str) -> List[Tuple[int, str]]:
    initial_forest = sorted([(freq, char) for char, freq in Counter(input).items()])
    codes = build_codes(build_tree(forest=initial_forest))
    print(codes)
    return ''.join(codes[char] for char in input)


if __name__ == "__main__":
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(0)

    #with open('NAI12/a.txt', 'r') as o:
        #test_units.append(o.readlines()[0])
    
    test_units.append(com(10000))
    for string in test_units:
        huffman(string)
