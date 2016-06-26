# The MIT License (MIT)
# Copyright (c) 2016 Ishita Takeshi

from math import log2


def entropy(probability):
    """Returns the entropy of a list of probabilities"""
    return sum(-p*log2(p) for p in probability if p > 0)


def average_code_length(code, probability):
    assert(code.keys() == probability.keys())
    return sum(probability[k] * len(code[k]) for k in probability.keys())


def test_entropy():
    assert(entropy([0.0, 1.0]) == 0.0)
    assert(entropy([0.5, 0.5]) == 1.0)


if __name__ == '__main__':
    test_entropy()
