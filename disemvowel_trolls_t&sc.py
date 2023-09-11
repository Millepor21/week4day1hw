# time: O(1) + O(N) => O(N) space: O(1) + O(N) => O(N)
def disemvowel(string_):
    vowel = 'aeiou' # time: O(1) space: O(1)
    nvc = [] # time: O(1) space: O(N)
    for letter in string_: # time: O(N) space: O(1)
        if letter.lower() not in vowel: # time: O(1) space: O(1)
            nvc.append(letter) # time: O(1) space: O(1)
    string_ = ''.join(nvc) # time: O(1) space: O(1)
    return string_ # time: O(1) space: O(1)

print(disemvowel("This website is for losers LOL!"))