import get_vocab_list
import get_long_sentences
from docx import Document

FILE_PATH_1 = './8-1-3 Telepathy.docx'
FILE_PATH_2 = './11-1-2 The Falkirk Wheel.docx'

PREVIEW_NUM = 20
PREVIEW_FILE_NAME = '阅读1-预习资料.docx'

QUIZ_NUM = 6
QUIZ_FILE_NAME = '阅读2-课首小测.docx'

SENTENCE_NUM = 2


def read_files(file_path_1, file_path_2):
    file_1 = Document(file_path_1)
    file_2 = Document(file_path_2)
    return file_1, file_2


def generate_preview(select_vocab_list, preview_file_name):
    preview = Document()
    preview.add_heading("课前预习")
    for word in select_vocab_list:
        preview.add_paragraph(word)
    preview.save(preview_file_name)


def generate_quiz(quiz_vocab_list, longest_sentences, quiz_file_name):
    quiz = Document()
    quiz.add_heading("单词")
    for word in quiz_vocab_list:
        quiz.add_paragraph(word)

    quiz.add_heading("长难句")
    for sentence in longest_sentences:
        quiz.add_paragraph(sentence)

    quiz.add_heading("同义转换")

    quiz.save(quiz_file_name)


file_1, file_2 = read_files(FILE_PATH_1, FILE_PATH_2)

all_bold_vocab = get_vocab_list.get_all_bold_vocab(file_1, file_2)
clean_vocab_list = get_vocab_list.clean_list(all_bold_vocab)
select_vocab_list = get_vocab_list.select_words(clean_vocab_list, PREVIEW_NUM)
generate_preview(select_vocab_list, PREVIEW_FILE_NAME)

quiz_vocab_list = get_vocab_list.select_words(select_vocab_list, QUIZ_NUM)
all_text = get_long_sentences.get_all_text(file_1, file_2)
all_sentences = get_long_sentences.split_text_to_sentences(all_text)
longest_sentences = get_long_sentences.select_longest_sentences(
    all_sentences, SENTENCE_NUM)
generate_quiz(quiz_vocab_list, longest_sentences, QUIZ_FILE_NAME)
