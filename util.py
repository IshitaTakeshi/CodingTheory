# The MIT License (MIT)
# Copyright (c) 2016 Ishita Takeshi

def show(code, probability):
    print("Symbol  Probability  Codeword")
    print("-----------------------------")
    for symbol in sorted(probability.keys()):
        print("{}       {:.2f}         {}".format(
              symbol, probability[symbol], code[symbol]))
    print("")
