import random

# Read all text from documents


def get_all_text(document_list):
    all_text = []
    for document in document_list:
        for para in document.paragraphs:
            for run in para.runs:
                all_text.append(run.text)
    return all_text

# Split text by period


def split_text_to_sentences(all_text):
    all_sentences = []
    # get rid of the title
    for para in all_text[1:]:
        sentences = para.split('.')
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence != '':
                sentence += '.'
                all_sentences.append(sentence)
    return all_sentences

# Select some long sentences


def select_longest_sentences(all_sentences, sentence_num):
    sort_list = sorted(all_sentences, key=len, reverse=True)[:5]
    return random.sample(sort_list, k=sentence_num)
