word = input()
word = word.lower()
word = word.translate({ord(i): None for i in 'aeiouy'})

number_of_letters = len(word)

letter = []

for x in word:
    letter.append('.')
    letter.append(x)


#print(letter)

number_of_loops = number_of_letters * 2

word_out = ''

for i in range(number_of_loops):
    word_out = word_out + letter[i]

print(word_out)
