import re

def read_signature():
    '''This function reads the values of linguistic features from the model and returns a signature to be compared with the provided texts'''
    print("Welcome to the automatic COH-PIAH detector.")
    print("Provide the typical signature of an infected student:")

    wal = float(input("Enter the average word length:"))
    ttr = float(input("Enter the Type-Token ratio:"))
    hlr = float(input("Enter the Hapax Legomena ratio:"))
    sal = float(input("Enter the average sentence length:"))
    sac = float(input("Enter the average sentence complexity:"))
    pal = float(input("Enter the average phrase length:"))

    return [wal, ttr, hlr, sal, sac, pal]

def read_texts():
    '''This function reads all the texts to be compared and returns a list containing each text as an element'''
    i = 1
    texts = []
    text = input("Enter text " + str(i) + " (press enter to exit):")
    while text:
        texts.append(text)
        i += 1
        text = input("Enter text " + str(i) + " (press enter to exit):")

    return texts

def separate_sentences(text):
    '''This function receives a text and returns a list of sentences within the text'''
    sentences = re.split(r'[.!?]+', text)
    if sentences[-1] == '':
        del sentences[-1]
    return sentences

def separate_phrases(sentence):
    '''This function receives a sentence and returns a list of phrases within the sentence'''
    return re.split(r'[,:;]+', sentence)

def separate_words(phrase):
    '''This function receives a phrase and returns a list of words within the phrase'''
    return phrase.split()

def count_unique_words(word_list):
    '''This function receives a list of words and returns the number of words that appear only once'''
    freq = dict()
    unique_count = 0
    for word in word_list:
        w = word.lower()
        if w in freq:
            if freq[w] == 1:
                unique_count -= 1
            freq[w] += 1
        else:
            freq[w] = 1
            unique_count += 1

    return unique_count

def count_different_words(word_list):
    '''This function receives a list of words and returns the number of different words used'''
    freq = dict()
    for word in word_list:
        w = word.lower()
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    return len(freq)

def compare_signatures(sig_a, sig_b):
    '''To be implemented. This function receives two text signatures and should return the degree of similarity between the signatures.'''
    similarity = 0
    for i in range(6):
        similarity += abs(sig_a[i] - sig_b[i])
    similarity /= 6

    return similarity

def calculate_signature(text):
    '''To be implemented. This function receives a text and should return the signature of the text.'''
    phrases = []
    words = []

    sentences = separate_sentences(text)
    for sentence in sentences:
        phrases = phrases + separate_phrases(sentence)
    for phrase in phrases:
        words = words + separate_words(phrase)

    avg_word_length = 0
    for word in words:
        avg_word_length += len(word)
    avg_word_length /= len(words)

    type_token_ratio = count_different_words(words) / len(words)

    hapax_legomena_ratio = count_unique_words(words) / len(words)

    avg_sentence_length = 0
    for sentence in sentences:
        avg_sentence_length += len(sentence)
    avg_sentence_length /= len(sentences)

    complexity_sentence = len(phrases) / len(sentences)

    avg_phrase_length = 0
    for phrase in phrases:
        avg_phrase_length += len(phrase)
    avg_phrase_length /= len(phrases)

    return [avg_word_length, type_token_ratio, hapax_legomena_ratio, avg_sentence_length, complexity_sentence, avg_phrase_length]

def evaluate_texts(texts, reference_signature):
    '''To be implemented. This function receives a list of texts and a reference signature and should return the number (1 to n) of the text with the highest probability of being infected with COH-PIAH.'''
    signatures = []
    for i in range(len(texts)):
        signatures.append(calculate_signature(texts[i]))

    most_similarity = compare_signatures(signatures[0], reference_signature)
    pos = 0
    for i in range(1, len(signatures)):
        if compare_signatures(signatures[i], reference_signature) < most_similarity:
            most_similarity = compare_signatures(signatures[i], reference_signature)
            pos = i
    
    return pos + 1

reference_signature = read_signature()
texts = read_texts()

print("The author of text", evaluate_texts(texts, reference_signature), "is infected with COH-PIAH")
