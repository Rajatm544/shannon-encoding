import math
# program to implement shannon encoding technique


# calculate the probabilties in descending order
def probabilty(freq, length):
    # calculate probabilty of each symbol
    prob = {}
    for letter in freq.keys():
        prob[letter] = freq[letter] / length

    # create a dict to store probabilties in descending order
    sorted_prob = dict(
        sorted(prob.items(), key=lambda item: item[1], reverse=True)
    )

    return sorted_prob


# function to calculate alpha values
def calculate_alpha(prob):
    alpha_values = [0]
    # calculate values of alpha i
    for i in range(1, len(prob)):
        alpha_values.append((alpha_values[i - 1] + prob[i - 1]))

    return alpha_values


# function to caluculate length values for each shannon code
def calculate_length(prob_value):
    i = 1
    while(True):
        if(2 ** i >= round((1 / prob_value))):
            return i
        i += 1


# function to convert fractional decimal to binary, for given length
def dec_to_bin(num, length):

    binary = ""
    # Fetch the integral part of decimal number
    Integral = int(num)

    # Fetch the fractional part decimal number
    fractional = num - Integral

    # Conversion of fractional part to binary equivalent
    while (length):

        # Find next bit in fraction
        fractional *= 2
        fract_bit = int(fractional)

        if (fract_bit == 1):
            fractional -= fract_bit
            binary += '1'
        else:
            binary += '0'

        length -= 1

    return binary


# function to calculate entropy of the given shannon codes
def calculate_entropy(prob):
    entropy = 0.0

    for value in prob:
        entropy += value * math.log2(1/value)

    return round(entropy, 4)


# function to calculate the average length of the shannon codes
def calculate_avg_length(prob, lenghts):
    L = 0.0

    for i in range(len(prob)):
        L += prob[i] * lenghts[i]

    return round(L, 4)


def main():
    # Input a string to perform shannon encoding
    str = input("Enter a string of characters to encode: ")
    str_length = len(str)

    # find the frequency of each symbol in the input
    freq = {}
    for letter in str:
        if(freq.get(letter)):
            freq[letter] += 1
        else:
            freq[letter] = 1

    # calculate the values for probability, alpha, and length of thr Shannon code for each symbol in the input
    probabilities = probabilty(freq, str_length)
    prob_values = list(probabilities.values())
    alphas = calculate_alpha(prob_values)

    lengths = []
    for prob in prob_values:
        lengths.append(calculate_length(prob))

    # calculate the shannon codes
    codes = []
    for i in range(len(alphas)):
        codes.append(dec_to_bin(alphas[i], lengths[i]))

    # Print the symbol and its encoded codeword
    symbols = list(probabilities.keys())

    print("\n-------------------------")
    print("Symbol   |   Shannon Code")
    print("-------------------------")

    for i in range(len(symbols)):
        print(f"{symbols[i]}        |   {codes[i]}")

    print("-------------------------\n")

    print("Following values indicate the performance of Shannon Encoding Algorithm:\n")
    # calculate and print the entropy
    entropy = calculate_entropy(prob_values)
    print(f"Entropy, H(s) = {entropy} bits/symbol")

    # calculate and print the Average length
    avg_length = calculate_avg_length(prob_values, lengths)
    print(f"Average length, L = {avg_length} bits")

    # calculate and print the efficiency and redundancy
    efficiency = entropy / avg_length * 100
    efficiency = round(efficiency, 2)
    redundancy = round(100 - efficiency, 2)

    print(f"Efficiency, η = {efficiency} %")
    print(f"Redundancy, R = {redundancy} %")


if __name__ == '__main__':
    main()
