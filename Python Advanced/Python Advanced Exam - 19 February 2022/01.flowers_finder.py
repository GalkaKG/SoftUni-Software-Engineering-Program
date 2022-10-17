# 1-st decision:

from collections import deque

vowels = deque(input().split())
consonants = input().split()

flowers_dict = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
word_found = False

while vowels and consonants and not word_found:
    vowel, consonant = vowels.popleft(), consonants.pop()

    for key, value in flowers_dict.items():
        if vowel in value:
            value = value.replace(vowel, '')
            flowers_dict[key] = value
        if consonant in value:
            value = value.replace(consonant, '')
            flowers_dict[key] = value

        if value == '':
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

word1 = 'rose'
word2 = 'tulip'
word3 = 'lotus'
word4 = 'daffodil'
copy_word_1 = word1
copy_word_2 = word2
copy_word_3 = word3
copy_word_4 = word4

founded_word = ''

while vowels and consonants:
    curr_vowel = vowels[0]
    curr_cons = consonants[-1]
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

    vowels.popleft()
    consonants.pop()

    if not word1:
        founded_word = copy_word_1
        break
    elif not word2:
        founded_word = copy_word_2
        break
    elif not word3:
        founded_word = copy_word_3
        break
    elif not word4:
        founded_word = copy_word_4
        break

if founded_word:
    print(f"Word found: {founded_word}")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
