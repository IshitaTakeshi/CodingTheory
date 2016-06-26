# The MIT License (MIT)
# Copyright (c) 2016 Ishita Takeshi


def sort_symbols(probability):
    symbols = probability.keys()
    return sorted(symbols, key=lambda k: probability[k], reverse=True)
