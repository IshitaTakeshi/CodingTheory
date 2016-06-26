from shannon_fano import shannon_fano
from shannon_fano_elias import shannon_fano_elias
from huffman import huffman
from metric import entropy, average_code_length
from prefixcode import isprefixcode
from util import show


probability = {
    "A": 0.18, "B": 0.08, "C": 0.15, "D": 0.12,
    "E": 0.3, "F": 0.02, "G": 0.1, "H": 0.05
}


print("# Symbols\n")
print("Symbol  Probability")
print("-------------------")
for symbol, p in probability.items():
    print("{}       {}".format(symbol, p))
print("\n")


print("# Shannon-Fano coding\n")
shannon_fano_code = shannon_fano(probability)
show(shannon_fano_code, probability)
isprefixcode(shannon_fano_code)
print("")

print("# Shannon-Fano-Elias coding\n")
shannon_fano_elias_code = shannon_fano_elias(probability, sort_symbols=True)
show(shannon_fano_elias_code, probability)
isprefixcode(shannon_fano_elias_code)
print("")

print("# Huffman coding\n")
huffman_code = huffman(probability)
show(huffman_code, probability)
isprefixcode(huffman_code)
print("")


print("Entropy of data                         : {:.3f} [bit]".format(
      entropy(probability.values())))

print("Average Shannon-Fano code length        : {:.3f} [bit]".format(
      average_code_length(shannon_fano_code, probability)))

print("Average Shannon-Fano-Elias code length  : {:.3f} [bit]".format(
      average_code_length(shannon_fano_elias_code, probability)))

print("Average Huffman code length             : {:.3f} [bit]".format(
      average_code_length(huffman_code, probability)))
