# time: O(N) space: O(1)
def get_count(sentence):
    count = 0# time: O(1) space: O(1)
    for letter in sentence:# time: O(N) space: O(1)
        if letter.lower() in 'aeiou':# time: O(1) space: O(1)
            count+=1# time: O(1) space: O(1)
    return count# time: O(1) space: O(1)

print(get_count("Should count all vowels"))