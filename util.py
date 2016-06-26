# The MIT License (MIT)
# Copyright (c) 2016 Ishita Takeshi

def show(probability, code):
    print("Symbol  Probability  Codeword")
    for symbol in sorted(probability.keys()):
        print("{}       {:.2f}         {}".format(
              symbol, probability[symbol], code[symbol]))
    print("")
