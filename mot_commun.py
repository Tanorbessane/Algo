def get_common_words(a,b):
    sentence_1 = a.lower().split(" ")
    sentence_2 = b.lower().split(" ")
    common_words = []
    for word in sentence_1:
        if word in sentence_2:
            common_words.append(word)
    return common_words

def get_common_words2(a,b):

    sentence_1 = set(a.lower().split(" "))
    sentence_2 = set(b.lower().split(" "))
    #return list(sentence_1.intersection(sentence_2))  
    return list(sentence_1 & sentence_2)
a = "bonjour je m'appelle Tanor"
b = "Bonjour je suis titi"

# print(get_common_words(a,b))
print(get_common_words2(a,b))
