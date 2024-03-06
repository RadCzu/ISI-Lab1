sentence = input('Enter a sentence: ')

# sentence2 = sentence
#
# takie podejście nie działa bo litery stringa nie można przypisać
# for letter in sentence2:
#     if letter == 'o':
#         sentence[sentence.find(letter)] = '0'
#     elif letter == 'e':
#         sentence[sentence.find(letter)] = '3'
#     elif letter == 'i':
#         sentence[sentence.find(letter)] = '1'
#     elif letter == 'a':
#         sentence[sentence.find(letter)] = '4'
#
# print(sentence2)

sentence = sentence.replace('o', '0')
sentence = sentence.replace('e', '3')
sentence = sentence.replace('i', '1')
sentence = sentence.replace('a', '4')

print(sentence)