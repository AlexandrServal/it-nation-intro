words = 'national aeronautics space administration'
print(words)
# new_words = words.split()
# print(new_words)
abbr = ''
for word in words.split():
    abbr += word[0]
    print(abbr)
new_abbr = abbr.upper()
print(new_abbr)