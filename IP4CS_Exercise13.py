# jiinso
# 11/06/2014
# IP4CS: In Class Exercise 13
# Write a recursive function to test if a string is a Palindrome.

# import string module
import string

# define a function Palindrome that checks if the inputted argument, sample (string type) is indeed a palindrome.
def Palindrome(sample):
    if len(sample) <= 1:										# if the length of the sample is 1, or 0 (from taking off the first and last letters through recursion)
    	return  "'%s' is a Palindrome." %S							# it is a palindrome.
    elif sample[0] == sample[-1]:								# else if the first letter of the sample corresponds with the last letter,
   	return Palindrome(sample[1:-1])							# call on the function Palindrome (recursion!) on the sample string without the first and last letters
    else:													# else (if the first and last letters are not the same)
    	return "'%s' is not a Palindrome." %S						# it is not a palindrome.
    	    	
    	
# create a string variable for user to input into, and change it to lowercase string so that comparison can be done
S = str(raw_input("Please input a word, phrase, or sentence you want to check if it is a Palindrome: "))
SL = S.lower()

# declare empty string variable called sample.
sample = ""

# for words in the lowercase string, append only words (no symbols, numbers, etc.) to the empty string 'sample'.
for w in SL:
    if w in string.lowercase:
    	 sample+= w

# use the sample to call on the Palindrome function and print out the results.
print Palindrome(sample)
