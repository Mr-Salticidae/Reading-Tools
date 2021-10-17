from docx import Document
import random

FILE_PATH_1 = './test1.docx'
FILE_PATH_2 = './test2.docx'
SENTENCE_NUM = 5
RESULT_FILE_NAME = 'reading.docx'


def get_all_text(file_1, file_2):
    all_text = []

    for para in file_1.paragraphs:
        for run in para.runs:
            all_text.append(run.text)

    for para in file_2.paragraphs:
        for run in para.runs:
            all_text.append(run.text)
    return all_text


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


def select_longest_sentences(all_sentences, sentence_num):
    sort_list = sorted(all_sentences, key=len, reverse=True)[:5]
    return random.sample(sort_list, k=sentence_num)


def write_sentences_to_file(longest_sentences, file_name):
    result = Document()
    for sentence in longest_sentences:
        result.add_paragraph(sentence)
    result.save(file_name)
