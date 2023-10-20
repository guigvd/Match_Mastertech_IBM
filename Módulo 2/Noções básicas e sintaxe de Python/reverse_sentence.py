# inverter palavras em uma determinada cadeia.

def rev_sentence(sentence):
    words = sentence.split(' ')

    reverse_sentence = ' '.join(reversed(words))

    return reverse_sentence

print(rev_sentence('Testando para ver se funciona'))