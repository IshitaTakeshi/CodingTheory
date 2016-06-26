def sort_symbols(probability):
    symbols = probability.keys()
    return sorted(symbols, key=lambda k: probability[k], reverse=True)

