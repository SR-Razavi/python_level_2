"""
    * regular expression allow au to search for patterns in python strings.
    * they can seem incredibly intimidating at first due to their strange syntax!
    * we'll walk through the basics of regular expressions, we will use them in django!
"""

import re # find pattern in text

patterns = ['term1', 'term2'] # so these are the patterns i am going to be loking for


# and then i'm going to have some text to actually parse
# so now has term one inside of it but it doesn't have the actule other term 
text = 'this is a string with term1, not not the other'

# and then what i'm going to do is say for patten in patterns 
for pattern in patterns:
    print("i'm searching for: " + pattern)

    # so let's show you how you can use the regular expressions
    # model to actully make that search.
    # so i'm first going to check if there's a match so i call ( re ) dot and then, 
    # the search function for that.
    if(re.search(pattern, text)):
        print('match!')
    else:
        print('no match!')
