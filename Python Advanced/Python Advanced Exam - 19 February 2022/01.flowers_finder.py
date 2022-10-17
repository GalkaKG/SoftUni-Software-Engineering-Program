# 1-st decision:

from collections import deque

vowels = deque(input().split())
consonants = input().split()

flowers_dict = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
word_found = False

while vowels and consonants and not word_found:
    vowel, consonant = vowels.popleft(), consonants.pop()

    for key in flowers_dict.keys():
        flowers_dict[key] = flowers_dict[key].replace(vowel, '')
        flowers_dict[key] = flowers_dict[key].replace(consonant, '')

        if flowers_dict[key] == '':
            word_found = True
            print(f'Word found: {key}')

if not word_found:
    print('Cannot find any word!')

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')

if consonants:
    print(f'Consonants left: {" ".join(consonants)}')


    
    

# 2-nd decision

from collections import deque

vowels = deque(input().split())
consonants = input().split()

word1, word2, word3, word4 = 'rose', 'tulip', 'lotus', 'daffodil'
copy_word_1, copy_word_2, copy_word_3, copy_word_4 = word1, word2, word3, word4

founded_word = ''
is_found_word = False

while vowels and consonants and not is_found_word:
    curr_vowel = vowels.popleft()
    curr_cons = consonants.pop()

    if curr_vowel in word1:
        word1 = word1.replace(curr_vowel, '')
    if curr_cons in word1:
        word1 = word1.replace(curr_cons, '')
    if curr_vowel in word2:
        word2 = word2.replace(curr_vowel, '')
    if curr_cons in word2:
        word2 = word2.replace(curr_cons, '')
    if curr_vowel in word3:
        word3 = word3.replace(curr_vowel, '')
    if curr_cons in word3:
        word3 = word3.replace(curr_cons, '')
    if curr_vowel in word4:
        word4 = word4.replace(curr_vowel, '')
    if curr_cons in word4:
        word4 = word4.replace(curr_cons, '')

    if not word1:
        founded_word, is_found_word = copy_word_1, True
    elif not word2:
        founded_word, is_found_word = copy_word_2, True
    elif not word3:
        founded_word, is_found_word = copy_word_3, True
    elif not word4:
        founded_word, is_found_word = copy_word_4, True

if founded_word:
    print(f"Word found: {founded_word}")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
