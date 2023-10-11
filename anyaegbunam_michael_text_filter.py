user_phrase = 'The Quick Brown Fox Jumps.'  
split_string = user_phrase.split()

print(user_phrase)
print(split_string)

banned_words = ['Fox', 'Dog', 'Turkey', 'Cat', 'Chicken']

for word in split_string:
    if word in banned_words:
        split_string.remove(word)


print(split_string)        

