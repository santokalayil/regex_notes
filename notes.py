import re

# reading a text - originally i have copied from my resume.pdf file to text
with open('resume.txt','r', encoding='utf-8') as f:
    text = f.read()

# ------------------------------------------------
'''
meta character that are needed to be escaped: . ^ $ * + ? { } [ ] \ | ( )

. - any character except new line
\d - Digit(0-9)
\D - not a digit(0-9)
\w - word character(a-z, A-Z, 0-9, _ )
\s - whitespace(space, tab, newline)
\S - not whitespace(space, tab, newline)

these are used in conjunction with above ones
\b - word boundary
\B - not a word boundary
^ - beginning of a string
$ - end of a string

metacharacters
[] - matches characters in brackets
[^ ] - matches characters not in

| - Either or 
() - group


quantifiers
* - 0 or more
+ - 1 or more
? - 0 or 1
{3} - exact number
{3,4} - range fo numbers(min and max)
'''
"""
meta character that are needed to be escaped: . ^ $ * + ? { } [ ] \ | ( )
"""
# function to easy
search = lambda raw_pattern: None==[print(match) for match in re.compile(raw_pattern).finditer(text)]
# None == is just for not showing all list outputs as None
search(r'.')

# =================================================================================================
#                                    SUPER PERFECT LOGIC
# =================================================================================================
print("UNIQUE STRING CHARACTERS")
print(100*"=")
print("".join(sorted(list(set(text))))) # this is a muxt find all unique characters then copy it as following)
print(100*"*")
pattern = re.compile(r'''(● )[a-zA-Z0-9\s"%&\'()+,-./:@’]*''')  # r for raw text
matches = pattern.finditer(text)
n = 0
for match in matches:
    new_start = False  # if new listing is not starting
    n += 1
#     string = str(text[match.span()[0]:match.span()[1]])
    string = match.group(0)  # other groups for  each groups specified by ()
    string = string.lstrip("●")
    string = " ".join(string.split("\n"))
    if ("KEY SKILLS" in string) or "PROFESSIONAL SUMMARY" in string:
        string = string.replace("KEY SKILLS", "").replace("PROFESSIONAL SUMMARY","")
        new_start = True  # since new section of list starts it becomes True
    string = " ".join(string.split())
    print(f"{n}, "+string)
    if new_start: # if new start is True then we need to restart the numbering
        print(100*"=")
        n = 0
    print(100*'-')

# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

subbed_urls = pattern.sub(r"\2", text) # second group
subbed_urls

# =====================================================================================================
# better working solution for web urls (avoiding email address also like ..@gmail.com)
search(r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})")

# another option but not workig for all
search(r"[(http://|https://)]*[a-zA-Z.]+\.(com|in|net)")

search(r"\d{2}[ -]\d{1,10}")  # {digit} - quantifier

search(r"\d\d[ .]\d") # seaches 2 digit and then any in " " or '.' and then 1 digit

search(r"\+\d\d[ ,]\d\d\d\d\d\d\d\d\d\d") # to search for phone number. space inside [] 
search(r"\+\d{2} \d{10}") # to search for phone number BEST METHOD

search(r"install$") # end of string
search(r"^SANTO") # start of string

search(r"\bsanto")  # shows all words that starts with 

search(r"\BNTO")  # if ends with
search(r"\Bkalayil")  # if ends wtih

search(r"\s") # if spaces of any kind like whitespace, space, linespace, tab etc.

search(r"\.")  # \.  for actual . textses:
# vs 
search(r".")   # all characters except linespaces

# ========================================= END ===========================================




