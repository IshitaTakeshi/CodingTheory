from copy import copy


def dangling_suffixes(code1, code2):
    def suffixes(code, word):
        N = len(word)
        s = set()
        for c in code:
            if c == word:
                continue
            if c.startswith(word):
                s.add(c[N:])
        return s

    ss = set()
    for c1 in code1:
        ss |= suffixes(code2, c1)
    for c2 in code2:
        ss |= suffixes(code1, c2)
    return ss


def isprefixcode(code):
    S0 = set(code)
    S = dangling_suffixes(S0, S0)
    D = dangling_suffixes(S0, S)

    while S != (S | D):
        S = S | D
        D = dangling_suffixes(S0, S)
    return len(S & S0) == 0


def run(S):
    if isprefixcode(S):
        print("{} is a prefix code.".format(S))
    else:
        print("{} is not a prefix code.".format(S))


if __name__ == '__main__':
    run(['0', '10', '101', '1100', '1110'])
    run(['0', '10', '1011', '1100', '1101'])
    run(['00', '0001', '001', '0011', '011'])
    run(['00', '1000', '11', '110', '1101'])
    run(['0000', '0001', '001', '01', '1'])
