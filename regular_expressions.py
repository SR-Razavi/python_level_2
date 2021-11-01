"""
    * regular expression allow au to search for patterns in python strings.
    * they can seem incredibly intimidating at first due to their strange syntax!
    * we'll walk through the basics of regular expressions, we will use them in django!
"""

import re # find pattern in text




# patterns = ['term1', 'term2'] # so these are the patterns i am going to be loking for

# and then i'm going to have some text to actually parse
# so now has term one inside of it but it doesn't have the actule other term 
# text = 'this is a string with term1, not not the other'

# and then what i'm going to do is say for patten in patterns 
# for pattern in patterns:
#     print("i'm searching for: " + pattern)

#     # so let's show you how you can use the regular expressions
#     # model to actully make that search.
#     # so i'm first going to check if there's a match so i call ( re ) dot and then, 
#     # the search function for that.
#     if(re.search(pattern, text)):
#         print('match!')
#     else:
#         print('no match!')




# now often you don't want the actule boolean value, you want the actule locations.
# (re.search) it is return actully not true or false, it returns a special matched type.
# it returns a match object.
# match = re.search('term1', text)

# return (<re.Match object; span=(22, 27), match='term1'>) it is regular expressions match object
# so what does it actually mean.
# it contains information about the match.
# so this object already contains information about where the match starts and the where the match ends.
# print(match) 

# second grab it just by saing this matched dot start close parentheses.
# now if i run this, now i can see it starts an index position 22 within the string.
# print(match.start())

# in regular expressions also have the ability to split a string on a particular pattern.
# split_term = '@'

# maybe we want to split somthing i can say that my phrase will just say e-mail is equal
# to user at gmail dot com.
# email = 'user@gmail.com'

# and then instead of (re.search) i can say (re.split) and then grab the split term and then 
# pasand the e-mail address
# print(re.split(split_term, email))

# and we have seen this before.
# this is actully built in already to string 
# so you could just say split as a method off of this on the at symbol.
# but it comes from the regular expression library.
# so just keep that in mind.
# email = 'user@gmail.com'.split('@')



# so we learn how to find the match and we learn how to do a split.
# now a lot time there are more complicated patterns that you're going to be looking for or maybe
# you want to find all the instances of a pattern and you can use are either find all the find all the 
# intances of pattern in a string, let me show you what.
# it just takes a pattern or a string and return of all non overlapping matches in the string.
# print(re.findall('match', 'test phrase match in middle')) # ['match']
# print(re.findall('match', 'test phrase match in match middle')) # ['match' , 'match]



# the idea here is not to memorize everything we show but just to be able to use it as reference.
# but let's start off by actully just showing an examples of multiple examples at once 
# actully we are going to create a helper function and this helper function is going to be called
# (multi_re_find) and what it is, it's going to take in a list of patterns and some phrase
# end then it is going to go.
def multi_re_find(patterns, phrase):
    for pat in patterns:
        print('serching for pattern {}'.format(pat))
        print(re.findall(pat, phrase))
        print('\n')

# so let's start off with repetition syntax and there are five ways to express repetition in a pattern.
# a pattern followed by the medak character asterix is repeated zero or more times.
test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

# i want find an (s) fallowed by zero or more these and keep in mind that kind of strange wording zero or more these.
# test_pattern = ['sd*']

# i pretty match get back every instance of where these is an 
# (['sd', 'sd', 's', 's', 'sddd', 'sddd', 'sddd', 'sd', 's', 's', 's', 's', 's', 's', 's', 'sddddd'])  
# wich makes sense because when you using the asterisks this returns (sd*) followed by anything repeated 
# zero or more time, several so essentially you are kind of asking for almost anything.
# anything that start an (s) at least.
# multi_re_find(test_pattern, test_phrase)

# so if we want it by one or more of these we put a plus sign.
# test_pattern = ['sd+']

# ['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sddddd']
# multi_re_find(test_pattern, test_phrase)

# now if i want it to be just zero or one time i can put a question mark.
# it is not helpfull but is avalible for you
# test_pattern = ['sd?']

# ['sd', 'sd', 's', 's', 'sd', 'sd', 'sd', 'sd', 's', 's', 's', 's', 's', 's', 's', 'sd']
# multi_re_find(test_pattern, test_phrase)

# you will probably want to know how do i define a specific counts.
# so let's say i want to know what is it followed by three (d) in (sd{3}) by ({}) pass number of you repetition you want.
# test_pattern = ['sd{3}']

# ['sddd', 'sddd', 'sddd', 'sddd']
# multi_re_find(test_pattern, test_phrase)

# if you want to specify tow numbers, maybe you are looking for one or there (d)
# test_pattern = ['sd{1,3}']

# ['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sddd']
# multi_re_find(test_pattern, test_phrase)



# fallowed by zero or more a plus sign.
# fallowed by one or more the question mark.
# fallowed by either zero or one and then the {} where you can define the actule number or pass in a list of numbers.



# say i want to find (s) followed by several letters or several sealer letters.
test_pattern = ['s[d]+']

# ['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sddddd']
multi_re_find(test_pattern, test_phrase)

# so i want to know where (s) is followed by either (s) or (d).
# so a again not together but separate here.
# so let me know is basically what i am asking here, where (s) is followed by one or more (s)'s or one or more (d)'s
test_pattern = ['s[sd]+']

# ['sdsd', 'sssddd', 'sdddsddd', 'sds', 'ssssss', 'sddddd']
multi_re_find(test_pattern, test_phrase)