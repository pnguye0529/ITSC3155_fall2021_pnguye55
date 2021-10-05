# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# needs to return the multiple of three that occurs the most in a string.
# For example, 0939639 would return 9 since it appeared 3 times while the
# other multiple of three appeared less than that. You only need to worry
# about single digit multiples of 3 (3, 6, 9). You must use a dictionary

def count_threes(n):
    # new dict
    d = dict()
    # traverse through the string n
    for i in n:
        # if current char is already a key in the dictionary, then increase the value of the key
        if i in d:
            d[i] += 1
        # if not, then set the current value of the key to 1
        else:
            d[i] = 1
    occ = max(d, key=d.get)
    return int(occ)


# longest_consecutive_repeating_char needs to account for the edge case where two characters have the same consecutive repeat length.
# The return value should now be a list containing all characters with the longest consecutive repeat.
# For example, the longest_consecutive_repeating_char('aabbccd') would return ['a', 'b', 'c'] (order doesn't matter).
def longest_consecutive_repeating_char(s):
    # create a new dictionary
    d = dict()
    # create variable count and temp char
    count = 0
    temp_char = ''
    # traverse through the string
    for char in s:
        # if the current character in s is = to temp
        if char == temp_char:
            # then the character is already seen, thus add 1 to count
            count += 1
            # then update the count for the current key
            d[char] = count
        # if the current char is not = to temp, then set the count to 1 since it is first seen
        else:
            count = 1
            # then set the temp character to current char
            temp_char = char
    # create a var ret that hold the max value within the dict
    ret = max(d, key=d.get)
    # return
    return ret


# # Part C. is_palindrome
# # Define a function is_palindrome(s) that takes a string s
# # and returns whether or not that string is a palindrome.
# # A palindrome is a string that reads the same backwards and
# # forwards. Treat capital letters the same as lowercase ones
# # and ignore spaces (i.e. case insensitive).
# def is_palindrome(s):
#     # remove all white space of string s and store it to the new variable str
#     str = s.replace(" ", "")
#     # declare a new variable tail and assign the last index of string s to it
#     tail = len(str) - 1
#     # start the loop from the first character to the middle character in the string s
#     for i in range(0, int(len(str) / 2)):
#         # compare the head and the tail character ignore the case
#         # using lower() function to compare the characters
#         if str[i].lower() != (str[tail - i].lower()):
#             # return false if any of the pair does not match
#             return False
#     # return true
#     return True
