from shannon_fano import shannon_fano
from shannon_fano_elias import shannon_fano_elias
from huffman import huffman
from util import show


probability = {
    "A": 0.18, "B": 0.08, "C": 0.15, "D": 0.12,
    "E": 0.3, "F": 0.02, "G": 0.1, "H": 0.05
}

print("Shannon-Fano coding")
print("-----------------------------")
code = shannon_fano(probability)
show(probability, code)
print("")

print("Shannon-Fano-Elias coding")
print("-----------------------------")
code = shannon_fano_elias(probability, sort_symbols=True)
show(probability, code)
print("")


print("Huffman coding")
print("-----------------------------")
code = huffman(probability)
show(probability, code)
print("")
