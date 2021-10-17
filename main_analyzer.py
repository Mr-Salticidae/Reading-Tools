import get_vocab_list
import get_long_sentences
from docx import Document
import os

SOURCES_FOLDER_PATH = './sources'
RESULTS_FOLDER_PATH = './results'

PREVIEW_NUM = 20
PREVIEW_FILE_NAME = '阅读1-预习资料.docx'

QUIZ_NUM = 6
QUIZ_FILE_NAME = '阅读2-课首小测.docx'

SENTENCE_NUM = 2


def get_all_files(sources_folder_path):
    file_list = []
    for root, dirs, files in os.walk(sources_folder_path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def read_document(file_list):
    document_list = []
    for file in file_list:
        document_list.append(Document(file))
    return document_list


def generate_preview(select_vocab_list, results_folder_path, preview_file_name):
    preview = Document()
    preview.add_heading("课前预习")
    for word in select_vocab_list:
        preview.add_paragraph(word)
    preview.save(os.path.join(results_folder_path, preview_file_name))


def generate_quiz(quiz_vocab_list, longest_sentences, results_folder_path, quiz_file_name):
    quiz = Document()
    quiz.add_heading("单词")
    for word in quiz_vocab_list:
        quiz.add_paragraph(word)

    quiz.add_heading("长难句")
    for sentence in longest_sentences:
        quiz.add_paragraph(sentence)

    quiz.add_heading("同义转换")

    quiz.save(os.path.join(results_folder_path, quiz_file_name))


file_list = get_all_files(SOURCES_FOLDER_PATH)
document_list = read_document(file_list)

all_bold_vocab = get_vocab_list.get_all_bold_vocab(document_list)
clean_vocab_list = get_vocab_list.clean_list(all_bold_vocab)
select_vocab_list = get_vocab_list.select_words(clean_vocab_list, PREVIEW_NUM)
generate_preview(select_vocab_list, RESULTS_FOLDER_PATH, PREVIEW_FILE_NAME)

quiz_vocab_list = get_vocab_list.select_words(select_vocab_list, QUIZ_NUM)
all_text = get_long_sentences.get_all_text(document_list)
all_sentences = get_long_sentences.split_text_to_sentences(all_text)
longest_sentences = get_long_sentences.select_longest_sentences(
    all_sentences, SENTENCE_NUM)
generate_quiz(quiz_vocab_list, longest_sentences,
              RESULTS_FOLDER_PATH, QUIZ_FILE_NAME)
