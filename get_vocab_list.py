import random

# Get bold text from documents


def get_all_bold_vocab(document_list):
    all_bold_vocab = []

    for document in document_list:
        for para in document.paragraphs:
            for run in para.runs:
                if run.bold:
                    all_bold_vocab.append(run.text)
    return all_bold_vocab

# Make vocab list clean


def clean_list(vocab_list):
    clean_list = []
    for vocab in vocab_list:
        vocab = vocab.lower().strip()
        clean_list.append(vocab)
    return list(set(clean_list))

# Select some words from vocab list


def select_words(clean_vocab_list, num):
    select_vocab_list = random.sample(clean_vocab_list, k=num)
    return select_vocab_list
