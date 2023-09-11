def get_count(sentence):
    count = 0
    for letter in sentence:
        if letter.lower() in 'aeiou':
            count+=1
    return count

print(get_count("Should count all vowels"))