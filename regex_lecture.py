'''
1. **Dot (.)**
    - The wildcard: Matches any single character except newline (`\n`).
    - Imagine it as a shape-shifter, able to become any character you need, just for a moment.
2. **Caret (^)**
    - The anchor for the start of a string.
    - Like a sentinel, standing guard at the beginning of your text.
3. **Dollar ($)**
    - The anchor for the end of a string.
    - The sentinel at the gates, ensuring nothing goes beyond the end of your text.
4. **Asterisk (*)**
    - Matches zero or more occurrences of the pattern left to it.
    - Think of it as a multiplier, creating copies of the character before it.
5. **Plus (+)**
    - Matches one or more occurrences of the pattern left to it.
    - Similar to the asterisk, but insists on at least one occurrence.
6. **Question Mark (?)**
    - It makes the preceding character optional.
    - It's the symbol of uncertainty, allowing flexibility in your patterns.
7. **Backslash (\)**
    - Escapes special characters or signals a special sequence.
    - The key to differentiating between a literal character and a magical symbol.
8. **Square Brackets ([])**
    - A set of characters. Matches any one character in the brackets.
    - Like choosing one tool from a toolbox, it selects one character from a set.
9. **Pipe (|)**
    - The OR operator. It matches either the pattern before or after it.
    - A fork in the road, giving you a choice between paths.
10. **Parentheses (())**
    - Groups patterns together and captures them.
    - Think of them as binding a spell, containing its power within.
11. **Curly Braces ({})**
    - Curly braces are used to define the exact number of times a character or a pattern must occur for a match to be found.
    - It's like telling your magic spell exactly how much power to use.
'''
### **Simple Exercises for Understanding**


'''
1.  **Dot (.) - The Wildcard Character**
    - **Task**: Find any three-character sequence in a text, where the middle character can be anything, the first has to be ‘c’ and the last has to be ‘t’.
    - **Regex Pattern**: `c.t`
    - **Test Sentence**: "I found a cat, a cot, and a cut in the room and the cat was cute, ctt cct coot colt"
    - **Expected Matches**: `['cat', 'cot', 'cut', cat, cut]`
    - **Explanation**: The dot `.` matches any single character (except newline), so it finds sequences where 'c' and 't' are separated by any character.
2. **Caret (^) - The Beginning Anchor**
    - **Task**: Find strings that start with 'Py'.
    - **Regex Pattern**: `^Py`
    - **Test Sentence**: "Python is fun"
    - **Expected Matches**: `[’Py’]` from 'Python' at the beginning of the sentence.
    - **Explanation**: The caret `^` ensures that the match must occur at the start of the string or line.
3. **Dollar ($) - The End Anchor**
    - **Task**: Identify strings that end with 'fun'.
    - **Regex Pattern**: `fun$`
    - **Test Sentence**: "Learning regex is fun"
    - **Expected Matches**: `['fun']` from 'Learning regex is fun.'
    - **Explanation**: The dollar `$` ensures that 'fun' is matched only if it's at the end of the string or line.
4. **Asterisk (*) - Zero or More Occurrences**
    - **Task**: Match a character followed by zero or more 'a's.
    - **Regex Pattern**: `ba*`
    - **Test Sentence**: "I saw a bat, and a ball in my bed, baaah!"
    - **Expected Matches**: `['ba', 'ba', 'b', 'baaa']` from ‘bat’, ‘ball’, ‘bed’, and ‘baaah!’.
    - **Explanation**: The pattern starts with the literal character 'b'. This means it will first look for occurrences of 'b' in the text. Following the 'b', we have 'a*'. Then, the asterisk  `*` which matches zero or more occurrences of the preceding character ('a' in this case).
5. **Plus (+) - One or More Occurrences**
    - **Task**: Find a character followed by one or more 'a's.
    - **Regex Pattern**: `ba+`
    - **Test Sentence**: "The battle of ba and baat."
    - **Expected Matches**: `['ba', 'ba', 'baa']` from ‘battle’, ‘ba’, and ‘baat’.
    - **Explanation**: The plus `+` matches one or more occurrences of the preceding character ('a' in this case).
6. **Question Mark (?) - Zero or One Occurrence**
    - **Task**: Match 'colour' or 'color'.
    - **Regex Pattern**: `colou?r`
    - **Test Sentence**: "The color is nice. I like this colour."
    - **Expected Matches**: `['color', 'colour']`
    - **Explanation**: The question mark `?` makes the preceding character ('u' in this case) optional.
7. **Backslash (\) - Escaping Special Characters**
    - **Task**: Match a period character in a sentence.
    - **Regex Pattern**: **`\.`**
    - **Test Sentence**: "End of sentence. Start of a new one."
    - **Expected Matches**: The periods `[.]` at the end of 'sentence.' and before 'Start'.
    - **Explanation**: In regex, the period (.) is a special character used as a wildcard. To match an actual period, the backslash **`\`** is used to escape the special meaning of the period, treating it as a literal character. The pattern **`\.`** specifically looks for the period character in the text.
8. **Square Brackets ([]) - Character Sets**
    - **Task**: Find all vowels in a word.
    - **Regex Pattern**: `[aeiou]`
    - **Another Pattern**: `[A-Za-z+]` - 
    - **Test Word**: "Regular"
    - **Expected Matches**: `['e', 'u', 'a']`
    - **Explanation**: The square brackets `[]` define a set of characters, any of which can be matched.
9. **Pipe (|) - The OR Operator**
    - **Task**: Match 'cat' or 'dog'.
    - **Regex Pattern**: `cat|dog`
    - **Test Sentence**: "I have a cat and a dog."
    - **Expected Matches**: `['cat', 'dog']`
    - **Explanation**: The pipe `|` acts as an OR operator, matching either the pattern before or after it.
10. **Parentheses (()) - Grouping**
    - **Task**: Find repetitions of 'woof' or 'meow'.
    - **Regex Pattern**: `(woof|meow)+`
    - **Test Sentence**: "The pets say woof woof and meow."
    - **Expected Matches**: `['woof’,  'woof', 'meow']`
    - **Explanation**: Parentheses `()` group patterns, allowing the plus `+` to apply to the entire group.
11. **Curly Braces ({}) - Specifying Exact Occurrences**
    - **Task**: Match a word where 'l' is followed by exactly two 'o's.
    - **Regex Pattern**: **`lo{2}`**
    - **Regex Pattern**: **`[L|lo{2}]`**
    - **Regex Pattern**: **`[A-Z|a-zo{2}]`**
    - **Test Sentence**: "Look at the loom and the balloon in the room, loser."
    - **Expected Matches**: ['loo', 'loo']
    - **Explanation**: The pattern **`lo{2}`** searches for an 'l' followed by exactly two 'o's. In our test sentence, it successfully identifies 'loo' within the words 'loom' and 'balloon', demonstrating the ability of curly braces **`{}`** to specify an exact number of occurrences.

'''

"""1. **\d - The Digit Hunter**
    - Hunts down digits (0-9) in your text.
    - It's like a metal detector that beeps only when it finds numbers.
2. **\w - The Word Wizard**
    - Finds word characters (letters, digits, and underscores).
    - Imagine it as a magnet that attracts only words and numbers, leaving everything else behind.
3. **\s - The Space Scout**
    - Seeks out whitespace (spaces, tabs, newlines).
    - Think of it as a radar that pings whenever it detects open space in your text.

### **Putting Special Sequences to the Test**

1. **The Digit Hunter in Action**:
    - **Task**: Extract all phone numbers from a text for a phone number in the format 'XXX-XXX-XXXX', where each 'X' is a digit
    - **Regex Pattern**: `\d{3}-\d{3}-\d{4}`
    - **Test Sentence**: "Call me at 123-456-7890 or 987-654-3210."
    - **Expected Matches**: `['123-456-7890', '987-654-3210']`
    - **Explanation**: The `\d` sequence finds digits, and `{3}` specifies exactly three digits. The hyphen `-` is a literal character, It separates different segments of the phone number. Overall, this pattern searches for sequences like a U.S. standard phone number format.
2. **The Word Wizard’s Spell**:
    - **Task**: Identify words containing numbers.
    - **Regex Pattern**: `\w+\d+\w*`
    - **Test Sentence**: "My username is user123 and my password is pass99word. my really cool username is Rhoadehouse10 fhosdhflsjdhfljsdhf"
    - **Expected Matches**: `['user123', 'pass99word', "Rhoadehouse]`
    - **Explanation**: `\w*` matches any word character zero or more times, and `\d` ensures there's at least one digit. This pattern finds words mixed with numbers.
3. **The Space Scout’s Exploration**:
    - **Task**: Split a sentence into words.
    - **Regex Pattern**: `\s+`
    - **Test Sentence**: "Welcome to the world of        regex!"
    - **Expected Matches**: The spaces between ' ', ' ', ' ', ' ', '        '’
    - **Explanation**: `\s+` matches one or more whitespace characters. It does not match the characters of the words themselves but the empty space that separates them, allowing us to see where one-word ends and another begins.

### **More Special Sequences**

1. **\D - The Non-Digit Detector**
    - Finds any character that is not a digit.
    - Like a filter that lets everything but coins pass through.
2. **\W - The Non-Word Character Identifier**
    - Matches any character that is not a word character (opposite of \w).
    - Imagine it as a tool that highlights everything in the text that isn't a word or number.
3. **\S - The Non-Whitespace Finder**
    - Identifies any character that is not a whitespace.
    - It's like a spotlight that ignores spaces and shines on everything else.
4. **\b - The Word Boundary Beacon** " as."
    pattern = "\b[as]\b
    - A marker for the positions between a word and a non-word character.
    - Think of it as a flare that lights up the borders of each word.
5. **\B - The Non-Word Boundary Signal**
    - Matches positions where a word boundary does not occur.
    - It’s the silent guardian that watches over continuous strings of word characters without interruption.
6. **\A - The Beginning Sentinel**
    - Matches only at the start of the string.
    - It’s like a gatekeeper that only allows patterns that appear right at the opening of your text.
7. **\Z - The End Guardian**
    - Matches only at the end of the string, before the final newline, if one exists.
    - Think of it as the final checkpoint at the very end of your textual journey.

### **Exercises to Master the Art**

1. **Task**: Find non-digit characters in a string.
    - **Regex Pattern**: **`\D+`**
    - **Test Sentence**: "Room 101 is on floor 3"
    - **Expected Matches**: `['Room ', ' is on floor ']`
    - **Explanation**: **`\D+`** matches one or more non-digit characters, capturing the words and spaces in the sentence.
2. **Task**: Identify characters that are not part of words.
    - **Regex Pattern**: **`\W`**
    - **Test Sentence**: "Hello, world! Are you ready?"
    - **Expected Matches**: `[',', ' ', '!', ' ', ' ', ' ', '?']`
    - **Explanation**: **`\W`** finds any character that is not a letter, digit, or underscore, like punctuation and spaces in this case.
3. **Task**: Identify non-whitespace characters in a string.
    - **Regex Pattern**: **`\S`**
    - **Test Sentence**: "Python 3.12 - New Features"
    - **Expected Matches**: Matches each non-space character individually, including letters, numbers, dots, and dashes.`['P', 'y', 't', 'h', 'o', 'n', '3', '.', '1', '2', '-', 'N', 'e', 'w', 'F', 'e', 'a', 't', 'u', 'r', 'e', 's']`
4. **Task**: Find words that start with 'py'.
    - **Regex Pattern**: **`\bPy\w*`**
    - **Test Sentence**: "Python is easy. Typing is fun.Python"
    - **Expected Matches**: `['Python']` from the beginning of the sentence.
    - **Explanation**: **`\b`** ensures the match starts at a word boundary, and **`\w*`** matches any word characters following 'Py'.
5. **Task**: Find instances of 'oo' not at the start or end of a word.
    - **Regex Pattern**: **`\Boo\B`**
    - **Test Sentence**: "The spooky moonlight illuminated the room."
    - **Expected Matches**: 'oo' in 'spooky', 'moonlight', and ‘room’.
    - **Explanation**:**`\B`** is used to find matches where a word boundary does not exist. In this case, it ensures that the pattern 'oo' is not at the start or end of a word. The regex pattern **`\Boo\B`** specifically looks for occurrences of 'oo' where both the preceding and following characters are also word characters (like letters or digits). It ignores cases where 'oo' is at the beginning or end of a word.
6. **Task**: Check if a string starts with 'Hello'.
    - **Regex Pattern**: **`\AHello`**
    - **Test Sentence**: "Hello, welcome to the world of Python! Hello again"
    - **Expected Matches**: `['Hello']` at the very beginning of the string.
    - **Explanation**: **`\AHello`** matches 'Hello' only if it appears at the start of the entire string.
7. **Task**: Match a pattern only if it's at the very end of the string.
    - **Regex Pattern**: **`Python\Z`**
    - **Test Sentence**: "Starting with basics and ending with Python"
    - **Expected Matches**: `['Python']` at the end of the sentence.
    - **Explanation**: **`Python\Z`** finds 'Python' as it's precisely at the end of the string, acting as a concluding marker."""

import re # imports the regular expression module

# re.findall() Retrieve all non-overlapping matches of a pattern in a string -  returns a list of matches
# "he el ll lo" "he ll"
# re.search() scan through a string, looking the first occurrence of the pattern - goes through the entirey of the string - returns a match object
# re.match() check only the start of the string for a match to the pattern - returns a match object
# re.split() split a string by pattern occurrences
# re.sub() replace occurrences of the pattern in a string with a replacement string

# . - wildcard
my_sentence = "I found a cat, a cot, and a cut in the room"
ct_words = re.findall(r"c.t", my_sentence) #r string - raw string so we are a little less restricted to python's string rules
print(ct_words) # ["cat", "cot", "cut"]
# search()
ct_words = re.search(r"c.t", my_sentence)
print(ct_words) # <re.Match object; span=(10, 13), match='cat'>
print(ct_words.group()) # returns the actual match from the match object when search finds something successfully
# ^^ "cat"
# match()
ct_words = re.match(r"c.t" , my_sentence)
print(ct_words) #None because it checks the start of the string and if no match is immediately found, we return None



# ^ caret - marks the start of the string
caret_pattern = r"^Py"
# caret_pattern = re.compile(r"^Py") #re.compile compile a pattern for us and we can save it to a variable to use over and over
my_sentence = "Python is Python fun"
matched_words = re.findall(caret_pattern, my_sentence)
print(matched_words) # ["Py"]

# $ matches at the end of a string
my_sentence = "Learning regex is fun"
matched_words = re.findall(r"fun$", my_sentence)
print(matched_words) #["fun"]

# * match 0 to many Occurrences of whatever character is to the left of it
my_sentence = "baaaa baaaaaaaaaaa black sheep, have you any wool? barber baby bubble and a bumble bee and also bar"
matched_words = re.findall(r"ba*", my_sentence)
print(matched_words) # ['baaaa', 'baaaaaaaaaaa', 'b', 'ba', 'b', 'ba', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'ba']
print(my_sentence)

# + 1 or more occurrences of the character preceding the +
my_sentece = "The battle of ba and baat it was bad and bitter"
matched_words = re.findall(r"ba+", my_sentece)
print(matched_words) # ['ba', 'ba', 'baa', 'ba']

# ? an optional occurrence - 0 or 1 time
my_sentence = "If you're American you say color and if you're European you say colour cor"
matched_words = re.findall(r"colou?r", my_sentence) #optional u, will match if its there or if its not
print(matched_words) # ['color', 'colour']

# sets []
word = "Regular"
matched_letters = re.findall(r"[aeiou]", word)
print(matched_letters) # ['e', 'u', 'a']

# my_sentence = "If you're American you say color and if you're European you say colour cor"
# matched_words = re.findall(r"colour", my_sentence)
# print(matched_words)

# | pipe is the or operator
my_sentence = "I have a cat and a dog and a birdbird"
matched_words = re.findall(r"cat|dog|bird", my_sentence)
print(matched_words) # ['cat', 'dog', 'bird']


# () for groups
import re
my_sentence = "the pet says woofwoof and meowmeowmeowmeow"
matched_words = re.findall(r"(woof|meow)+", my_sentence)
print(matched_words) # ['woof', 'woof', 'meow', 'meow', 'meow', 'meow']


# {} - specifying exact occurrences
# range of occurrences 
my_sentence = "Look at the loom and the ballooooooon in the room lololo lo"
matched_words = re.findall(r"lo", my_sentence)
print(matched_words) #['loo', 'loo']

# {2} -> something that happens exactly 2 times
# {2,} -> something occuring at least 2 times or at least as many times as we're specifying
# {2, 4} -> something occurring between 2 and 4 times

# \b matches a boundary between a word character and a non word character
my_sentence = "black cat tomcat certificate catfish"
matched_cat = re.findall(r"\bcat\b", my_sentence)
print(matched_cat) # only cat from black cat

# \B matches a boundary between two word characters

# \w matches any word character, letter, number, underscore
# looking for usernames
my_sentence = "My username is user123 and my password is pass99word"
matched_words = re.findall(r"\w+\d\w*", my_sentence)
print(matched_words) # ['user123', 'pass99word']

# \d matches any number character - only numbers
my_sentence = "Call me at 123-456-7891 or 987-654-3210"
matched_digits = re.findall(r"\d{3}-\d{3}-\d{4}", my_sentence)
print(matched_digits)

# using sets
matched_digits = re.findall(r"[0-9]{3}-[0-9]{3}-[0-9]{4}", my_sentence)
print(matched_digits)

# checking for an email in a string
text = "Contact us at suppóóúñärt@example.com or sales_are_cool.yolo@example.com or cool_person56@gmail.edu coolpersongmail.o"
# combine multiple characters and chacter ranges in a set
# A-Z any capital letter
# a-z any lower case letter
# 0-9 any number between 0-9
# [A-Za-z0-9] any combination of capital,lower case letters and numbers
# [A-Za-z0-9._%+-] combination of the above and any of the listed special characters
# . DOT in a set is read as a period
# [A-Za-z0-9._%+-]+ <-- this combination of characters happens at least 1 time - one or many occurrences
#                             username       @ website name  .   com or edu or org or whatever comes after the .
email_pattern = re.compile(r"\b[A-Za-z0-9À-ÿ._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b")
#  \u0300-\u036F  À-ÿ                                                        \. read literally as a dot not a wildcard because its outside of a set
emails = re.findall(email_pattern, text)
print(emails)

# validating user input - collecting an email and making sure its adhering to a specific pattern
# email = input("Please enter your email").lower().strip()
# if re.match(email_pattern, email):
#     print("Valid Email Adress")
# else:
#     print("Please check your email and try again")

# accessing the matched group from the match object
# validating email and adding it to a dictionary as the key, with an empty dictionary as the value
# email_pattern = re.compile(r"\b[A-Za-z0-9À-ÿ._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b")
# address_book = {}
# email = input("Please enter your email").lower().strip()
# match = re.match(email_pattern, email)
# # checking that our email is valid but checking if match is truthy
# # checking that match is not None
# if match:
#     print(f"Valid email: {match.group()}")
#     name = input("What is the name of your contact? ")
#     address_book[email] = {"name": name}
#     print(address_book)
# else:
#     print("Invalid Email Please try again")

# checking for a valid phone number
text = "Contact us at 123-456-7890"
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print(f"Phone Number Found: {match.group()}")

# excluding something
# ! <- not this thing
# list comprehension give me all of the things from the findall except for ones where this exists
# list comprehension and excluse phone number

matched_nums = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print(matched_nums)
# ['630-824-7768', '123-456-7891', '321-654-8744', '456-124-9635'] <- returned list from the findall
phone_numbers = [number for number in matched_nums if "630-824-7768" not in number ]
print(phone_numbers)

phone_numbers = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print(phone_numbers)

text = "Here are some neat emails except for yamama@gmail.com we got cool_guy420@hotmail.com business_person@yahoo.com coder_guy@codingtemple.com"

emails= re.findall(r"\b[A-Za-z0-9À-ÿ._%+-]+@(?!gmail\.com)[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", text)
print(emails)


print(re.findall(r"\b(?!630-824-7768)(\d{3}-\d{3}-\d{4})", text))

    

text = "I have so many friends they call me at  their numbers are 123-456-7891 321-654-8744, 456-124-9635 630-824-7768"
# list comprehension because findall is going to return a list of valid phonenumbers
# BUT i only want phone numbers returned that are not equal to my phone number
# \blooking for a boundary betweetn a word character and a non-word character
#?! - ignore the following pattern with the group
# (\d{3}-\d{3}-\d{4}) business as usual checking for phone numbers with a specific amount of digits

print(re.findall(r"(?!630-824-7768)(\d{3}-\d{3}-\d{4})", text))



text = "Here are some neat emails except for yamama@gmail.edu we got cool_guy420@hotmail.com business_person@yahoo.com coder_guy@codingtemple.com"

emails= re.findall(r"\b[A-Za-z0-9À-ÿ._%+-]+@[A-Za-z0-9.-]+(?!.com)\.[A-Za-z0-9]{2,}\b", text)
print(emails)

# using the ^ Check the beginning of the string
text = "Hello, world!"
if re.match(r"^Hello", text):
    print("The string starts with 'Hello")
else:
    print("it does not start with hello!")

# finding hashtags from twitter or instagram
post = "I love coding so much. My instructor is so amazing and handsome and is good at super smash #blessed #codinglyfe #yolo #gottagofast"
hashtags = re.findall(r"#\w+", post)
print(hashtags)
for hashtag in hashtags:
    print(f"{hashtag} is trending")


# extract the year from a date
sentence = "The event was held on 15/06/2014"
match = re.search(r"\b\d{4}\b", sentence)
if match:
    print(f"Year extracted..... {match.group()}")

# re.split()
text = "Python,Regex;Splitting-Examples. Fun, right?"
words = re.split(r"[,;.\s-]", text)
print(words)


# re.sub() - replace charactesr in the string
phone = "Phone: +1 (123) 456-7890"
standard_phone = re.sub(r"\D", "", phone)
print(standard_phone)

# replacing html tags
html = "<p>This is <em>HTML</em> content!</p>"
clean_text = re.sub(r"<.*?>", "", html)
print(clean_text)

# reformatting a date
date_string = "Today's date is 09/05/2024"
                    #groups   1       2      3         3   2  1
formatted_date = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\2-\1-\3", date_string)
print(formatted_date)


