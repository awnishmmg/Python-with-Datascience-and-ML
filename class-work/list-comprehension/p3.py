#find the documents,word tokenize,vocablary and grammer

document =  '''Awnish Likes sunny and Sunny likes awnish'''
words_tokens = [word.strip().lower() for word in document.split()]

print(words_tokens)
weight  = len(words_tokens)
frequency = [len(word) for word in words_tokens]

print('frequency of words:',frequency)
print('weight of the words:',weight)

vocablary = set(words_tokens)

print('vocablary(unique words):',vocablary)
weight_vocablary = len(vocablary)

print('weight of vocabs:',weight_vocablary)

frequency_vocabs = [len(u_word) for u_word in list(vocablary)]
print('frequency of vocabs:',frequency_vocabs)

#grammer : Rule of Vocabs 
grammer = frozenset(vocablary)
print('Grammer:',grammer)
 