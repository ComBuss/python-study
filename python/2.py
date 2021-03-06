def break_words(stuff):
    """이 함수는 문자열을 단어로 쪼개 줍니다."""
    words = (stuff.split(' '))
    return words

def sort_words(words):
    """단어를 정렬 합니다"""
    return sorted(words)

def print_first_word(words):
    """첫 단어를 꺼내서 출력합니다"""
    word = words.pop(0)
    return word

def print_last_word(words):
    word = words.pop(-1)
    return word

def sort_sentence(sentence):
    """한문장을 통째로 받아 단어를 정령해서 반환"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
