# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
    # if the number is divisible by 3 then return the division n/3
    if n % 3 == 0:
        return int(n / 3)
    # if not, return 0
    return 0


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
    s_length = len(s)
    counter = 0
    temp_count = 1
    character = s[0]
    for i in range(s_length):
        for j in range(i+1, s_length):
            if(s[i] != s[j]):
                break
            temp_count += 1

        if temp_count > counter:
            counter = temp_count
            character = s[i]
    return character


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
    # remove all white space of string s and store it to the new variable str
    str = s.replace(" ", "")
    # declare a new variable tail and assign the last index of string s to it
    tail = len(str) - 1
    # start the loop from the first character to the middle character in the string s
    for i in range(0, int(len(str) / 2)):
        # compare the head and the tail character ignore the case
        # using lower() function to compare the characters
        if str[i].lower() != (str[tail - i].lower()):
            # return false if any of the pair does not match
            return False
    # return true
    return True
