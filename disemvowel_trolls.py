def disemvowel(string_):
    vowel = 'aeiou'
    nvc = []
    for letter in string_:
        if letter.lower() not in vowel:
            nvc.append(letter)
    string_ = ''.join(nvc)
    return string_

print(disemvowel("This website is for losers LOL!"))