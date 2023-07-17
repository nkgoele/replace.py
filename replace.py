##Save the sentence The!quick!Brown!Fox!Jumps!Over!the!Lazy!dog
##Assign the variable s1 to the sentence above 
##Remove all the exclamation marks(!) in the sentence
##Assign the variable s2 to the new sentence above 
##Print s2
##Print the original sentence s1 in reverse

##Reprinting the sentence without the exclamation marks
s = """The!quick!Brown!Fox!Jumps!Over!the!Lazy!dog			
"""
print(s1.replace('!', ' ')) 

##Reprinting the new sentence without the exclamation marks in UPPER CASE format
s2 = (s.replace('!', ' ')) 
print(s2.upper())

##Print the original sentence in reverse
print(s[44:0:-1])





