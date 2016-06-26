from util import show
from numeric import sort_symbols
from prefixcode import isprefixcode


class AbstractNode(object):
    isleaf = None
    value = None


class Node(AbstractNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.value = left.value + right.value
        self.isleaf = False


class Leaf(AbstractNode):
    def __init__(self, symbol, probability):
        self.symbol = symbol
        self.value = probability
        self.isleaf = True


def make_tree(probability):
    nodes = [Leaf(s, p) for s, p in probability.items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda node: node.value)
        nodes = [Node(nodes[0], nodes[1])] + nodes[2:]
    return nodes[0]


def traverse(node, codeword="", code={}):
    if node.isleaf:
        code[node.symbol] = codeword
        return code

    code = traverse(node.left, codeword+"0", code)
    code = traverse(node.right, codeword+"1", code)
    return code


def huffman(probability):
    root = make_tree(probability)
    code = traverse(root)
    return code


def test_huffman():
    probability = {"A": 0.10, "B": 0.15, "C": 0.30, "D": 0.16, "E": 0.29}
    code = huffman(probability)
    expected = {"A": "010", "B": "011", "C": "11", "D": "00", "E": "10"}
    assert(code == expected)
    assert(isprefixcode(code))


if __name__ == '__main__':
    test_huffman()
    probability = {
        "A": 0.18, "B": 0.08, "C": 0.15, "D": 0.12,
        "E": 0.3, "F": 0.02, "G": 0.1, "H": 0.05
    }
    code = huffman(probability)
    assert(isprefixcode(code))
    show(probability, code)
