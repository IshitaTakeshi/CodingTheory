def split(probability, sorted_symbols):
    split_point = 1
    min_diff = float('inf')
    for i in range(1, len(sorted_symbols)-1):
        left = sum(probability[k] for k in sorted_symbols[:i])
        right = sum(probability[k] for k in sorted_symbols[i:])
        diff = abs(left-right)
        if diff < min_diff:
            split_point = i
            min_diff = diff
    return split_point


def sort_symbols_by_value(probability):
    symbols = probability.keys()
    return sorted(symbols, key=lambda k: probability[k], reverse=True)


def assign_digit(code, symbols, digit):
    for symbol in symbols:
        code.setdefault(symbol, "")
        code[symbol] += digit
    return code


def shannon_fano_(probability, sorted_symbols, code={}):
    if len(sorted_symbols) == 1:
        return code

    split_point = split(probability, sorted_symbols)
    L = sorted_symbols[split_point:]
    R = sorted_symbols[:split_point]

    assign_digit(code, L, "1")
    code = shannon_fano_(probability, L, code)

    assign_digit(code, R, "0")
    code = shannon_fano_(probability, R, code)

    return code


def shannon_fano(probability):
    return shannon_fano_(probability, sort_symbols_by_value(probability))


def show(probability, code):
    print("Symbol  Probability  Codeword")
    for symbol in sorted(probability.keys()):
        print("{}       {:.2f}         {}".format(
              symbol, probability[symbol], code[symbol]))
    print("")


def test_shannon_fano():
    occurrences = {"A": 15, "B": 7, "C": 6, "D": 6, "E": 5}
    probability = {}
    for symbol in occurrences.keys():
        probability[symbol] = occurrences[symbol] / sum(occurrences.values())

    code = shannon_fano(probability)

    # there are 2 patterns of code since occurrences of C and D are same
    expected1 = {"A": "00", "B": "01", "C": "10", "D": "110", "E": "111"}
    expected2 = {"A": "00", "B": "01", "C": "110", "D": "10", "E": "111"}
    assert(code == expected1 or code == expected2)


test_shannon_fano()

probability = {
    "A": 0.18, "B": 0.08, "C": 0.15, "D": 0.12,
    "E": 0.3, "F": 0.02, "G": 0.1, "H": 0.05
}
code = shannon_fano(probability)
show(probability, code)
