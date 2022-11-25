def remove_blank_string(text):
    while '' in text:
        text.remove('')
    return text


def function_separator(text): pass


with open('genii_Makarenko_1.txt', 'r', encoding='UTF-8') as file:
    file = file.read()
    sentences = file.split('\n')

    intermediate_sentences = []
    final_sentences = []

    for sentence in sentences:
        # sentence = sentence[:-1]  # remove '\n' sign
        if '?' in sentence:
            # sentence = sentence.replace('?', '+?')
            inner_sentence = sentence.replace('?', '+?').split('?')
            for single_sentence in inner_sentence:
                # single_sentence = single_sentence.replace('\n', '').replace('+', '?')
                # single_sentence = single_sentence.replace('+', '?')
                # intermediate_sentences.append(single_sentence.strip())
                intermediate_sentences.append(single_sentence.replace('\n', '').replace('+', '?').strip())
        elif '!' in sentence:
            # sentence = sentence.replace('!', '+!')
            inner_sentence = sentence.replace('!', '+!').split('!')
            for single_sentence in inner_sentence:
                # single_sentence = single_sentence.replace('\n', '').replace('+', '!')
                # single_sentence = single_sentence.replace('+', '!')
                intermediate_sentences.append(single_sentence.replace('\n', '').replace('+', '!').strip())
                # intermediate_sentences.append(single_sentence.strip())
        else:
            intermediate_sentences.append(sentence.strip())

    # while '' in intermediate_sentences:
    #     intermediate_sentences.remove('')
    intermediate_sentences = remove_blank_string(intermediate_sentences)

    for i in intermediate_sentences:
        print(i)
