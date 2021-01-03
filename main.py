import math
import string


def is_palindrome(p_input):
    l_input = p_input.lower()
    # if our input is a phrase we want to remove any white space that could interfere with parsing
    l_input = l_input.replace(" ", "")
    # any punctuation should be ignored
    punctuation = string.punctuation
    # Possible expensive runtime
    for punc in punctuation:
        l_input = l_input.replace(punc, "")
    length = len(l_input)
    # check for invalid input
    if length <= 1:
        # print(False, "Not a Valid word")
        return False
    middle = math.ceil(length / 2)
    # Our logic doesn't work for words less than 4 b/c middle == length - 1 if length <= 3
    if length <= 3:
        if l_input[0] != l_input[length - 1]:
            # print(False, " Input had a length <= 3 and chars did not match")
            return False
        else:
            # print(True, " Input", p_input, "had a length <= 3 and chars matched")
            return True
    # print("middle = ", middle, "For input: ", p_input)
    for char in l_input:
        length -= 1
        if length <= middle:
            # print(True, "Input: ", p_input, " is a palindrome")
            return True
        if char != l_input[length]:
            # print(False, "Input: ", p_input, " is not a palindrome")
            return False
