# Trouver le mot le court et le plus long dans une phrase
def find_min_word(string):
    s_split=string.split()
    minWord = s_split[0]
    for word in s_split:
        if len(word)<len(minWord):
            minWord = word
    return minWord
def find_max_word(string):
    s_split = string.split()
    max_word=s_split[0]
    for word in s_split : 
        if len(word) > len(max_word):
            max_word = word
    return max_word
def get_min_and_max_words(sentence):
    s_split = sentence.split()
    max_word =max(s_split,key=len)
    min_word = min(s_split,key=len)
    return(max_word,min_word)
# Trouver le mot le court et le plus long dans une phrase
# le premier par ordre alphabétique
def get_min_and_max_words_sorted(sentence):
    words = sentence.split("")
    min_word,max_word = get_min_and_max_words(sentence)
    all_min_words = [w for w in words if len(w) == len(min_word)]
    all_max_words = [w for w in words if len(w)==len(max_word)]
    all_max_words.sort()
    all_min_words.sort()
    return all_max_words[0], all_min_words[0]

def get_min_and_max_words_sorted2(sentence):
    s_split = sentence.split()
    s_split.sort()
    max_word =max(s_split,key=len)
    min_word = min(s_split,key=len)
    return(max_word,min_word)

s = "U chasseur sachant chasser sait chasser sans son chien"
print(find_min_word(s))
print(find_max_word(s))
max,min=get_min_and_max_words(s)
print("Le plus long mot est",max)
print("Le plus court mot est",min)
