"""
Дан файл состоящий из нескольких предложений. Нужно найти длину наименьшего и наибольшего предложение и вывести их длины и сами предложения
"""

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


with open('genii_Makarenko_1.txt', 'r', encoding='UTF-8') as file:
    file = file.read()
    sentences = file.split('\n')

    for sentence in sentences:
        function_separator(sentence, '!')
        function_separator(sentence, '?')
        if '!' not in sentence and '?' not in sentence:
            intermediate_sentences.append(sentence.strip())
        # if '?' in sentence:
        #     inner_sentence = sentence.replace('?', '+?').split('?')
        #     for single_sentence in inner_sentence:
        #         intermediate_sentences.append(single_sentence.replace('\n', '').replace('+', '?').strip())
        # elif '!' in sentence:
        #     inner_sentence = sentence.replace('!', '+!').split('!')
        #     for single_sentence in inner_sentence:
        #         intermediate_sentences.append(single_sentence.replace('\n', '').replace('+', '!').strip())
        # else:
        #     intermediate_sentences.append(sentence.strip())

    intermediate_sentences = remove_blank_string(intermediate_sentences)

    for i in intermediate_sentences:
        print(i)
