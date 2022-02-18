n = input()
n = int(n) 

list_of_words = []

for x in range(n):
    word_in = input()
    length_of_word = len(word_in)
    if length_of_word <= 10:
        list_of_words.append(word_in)
    else:
        p = length_of_word - 2
        word_in = word_in[:1] + str(p) + word_in[(length_of_word-1):]
        list_of_words.append(word_in)

print()

for word_out in list_of_words:
    print(word_out)

