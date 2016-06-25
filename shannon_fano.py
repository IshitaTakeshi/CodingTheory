from math import log2, ceil


def split(symbols, sorted_keys):
    split_point = 1
    min_diff = float('inf')
    for i in range(1, len(sorted_keys)-1):
        left = sum(symbols[key] for key in sorted_keys[:i])
        right = sum(symbols[key] for key in sorted_keys[i:])
        diff = abs(left-right)
        if diff < min_diff:
            split_point = i
            min_diff = diff
    return split_point


def sort_keys_by_value(symbols):
    return sorted(symbols.keys(), key=lambda k: symbols[k], reverse=True)


def assign_digit(code, keys, digit):
    for key in keys:
        code.setdefault(key, "")
        code[key] += digit
    return code

def shannon_fano_(symbols, sorted_keys, code={}):
    if len(sorted_keys) == 1:
        return code

    split_point = split(symbols, sorted_keys)
    L = sorted_keys[split_point:]
    R = sorted_keys[:split_point]

    assign_digit(code, L, "1")
    code = shannon_fano_(symbols, L, code)

    assign_digit(code, R, "0")
    code = shannon_fano_(symbols, R, code)

    return code


def shannon_fano(symbols):
    return shannon_fano_(symbols, sort_keys_by_value(symbols))


def test_wikipedia():
    occurrences = {"A": 15, "B": 7, "C": 6, "D": 6, "E": 5}
    symbols = {}
    for key in occurrences.keys():
        symbols[key] = occurrences[key] / sum(occurrences.values())

    code = shannon_fano(symbols)
    expected1 = {"A": "00", "B": "01", "C": "10", "D": "110", "E": "111"}
    expected2 = {"A": "00", "B": "01", "C": "110", "D": "10", "E": "111"}
    assert(code == expected1 or code == expected2)


test_wikipedia()
