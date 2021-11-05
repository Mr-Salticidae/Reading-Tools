import os
import docx2txt
from nltk.tokenize import word_tokenize, RegexpTokenizer

SOURCES_FOLDER_PATH = './sources'
RESULTS_FOLDER_PATH = './results'

# Get all file names in the sources folder


def get_all_files(sources_folder_path):
    file_list = []
    for root, _, files in os.walk(sources_folder_path):
        for file in files:
            if file.endswith('.docx'):
                file_list.append(os.path.join(root, file))
    return file_list

# Read all files


def read_all_files(file_list):
    dataset = []
    for file in file_list:
        dataset.append(docx2txt.process(file))
    return dataset

# Clean the dataset


def clean_dataset(dataset):
    corpus = []
    for article in dataset:
        # Get rid of bold
        article = article.replace(u'\xa0', u' ')

        # Get rid of \n and the space
        article = article.replace(u'\n', u' ')
        article = article.split(r"\n|[' ']")
        article = article[0]

        # Lower every word
        article = article.lower()

        corpus.append(article)
    return corpus

# Tokenize the corpus


def tokenize_corpus(corpus):
    tokens = []
    tokenizer = RegexpTokenizer(r'\w+')
    for article in corpus:
        tokens_per_article = tokenizer.tokenize(article)
        for token in tokens_per_article:
            tokens.append(token)
    return tokens


file_list = get_all_files(SOURCES_FOLDER_PATH)
dataset = read_all_files(file_list)
corpus = clean_dataset(dataset)
tokens = tokenize_corpus(corpus)
