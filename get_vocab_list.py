import random
from docx import Document

SOURCE_PATH = './vocab.txt'
PREVIEW_PATH = './clean_vocab.txt'
QUIZ_PATH = './quiz_vocab.txt'
PRIVIEW_NUM = 20
QUIZ_NUM = 6


def get_all_bold_vocab(file_1, file_2):
    all_bold_vocab = []

    for para in file_1.paragraphs:
        for run in para.runs:
            if run.bold:
                all_bold_vocab.append(run.text)

    for para in file_2.paragraphs:
        for run in para.runs:
            if run.bold:
                all_bold_vocab.append(run.text)

    return all_bold_vocab


def read_source_vocab_list(source_path):
    with open(source_path, 'r') as file:
        data = file.readlines()
        return data


def clean_list(vocab_list):
    clean_list = []
    for vocab in vocab_list:
        vocab = vocab.lower()
        clean_list.append(vocab)
    return list(set(clean_list))


def select_words(clean_vocab_list, num):
    select_vocab_list = random.sample(clean_vocab_list, k=num)
    return select_vocab_list
