import random
SOURCE_PATH = './vocab.txt'
PREVIEW_PATH = './clean_vocab.txt'
QUIZ_PATH = './quiz_vocab.txt'
PRIVIEW_NUM = 20
QUIZ_NUM = 6


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


def write_select_vocab_list_to_file(select_vocab_list, target_path):
    with open(target_path, 'w') as file:
        for vocab in select_vocab_list:
            file.writelines(vocab)


vocab_list = read_source_vocab_list(SOURCE_PATH)
clean_vocab_list = clean_list(vocab_list)
select_vocab_list = select_words(clean_vocab_list, PRIVIEW_NUM)
write_select_vocab_list_to_file(select_vocab_list, PREVIEW_PATH)

quiz_vocab_list = select_words(select_vocab_list, QUIZ_NUM)
write_select_vocab_list_to_file(quiz_vocab_list, QUIZ_PATH)
