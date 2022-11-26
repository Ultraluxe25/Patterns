intermediate_sentences = []
final_sentences = []


def remove_blank_string(text):
    while '' in text:
        text.remove('')
    return text


def function_separator(text, sign):
    if sign in text:
        text = text.replace(sign, '+' + sign).split(sign)
        for single_sentence in text:
            intermediate_sentences.append(single_sentence.replace('\n', '').replace('+', sign).strip())


def dot_separator(intermediate_sentences, sign):
    for sentence in intermediate_sentences:
        if sign in sentence:  # and (not sentence[sentence.index(sign) - 1].isupper()):
            sentence = sentence.replace(sign, '+' + sign).split(sign)
            for single_sentence in sentence:
                final_sentences.append(single_sentence.replace('\n', '').replace('+', sign).strip())


with open('genii_Makarenko_1.txt', 'r', encoding='UTF-8') as file:
    file = file.read()
    sentences = file.split('\n')

    for sentence in sentences:
        function_separator(sentence, '!')
        function_separator(sentence, '?')
        dot_separator(intermediate_sentences, '.')
        # if '!' not in sentence and '?' not in sentence:
        #     intermediate_sentences.append(sentence.strip())

    final_sentences = remove_blank_string(final_sentences)

    for i in final_sentences:
        print(i)
