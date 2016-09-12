# -* coding: utf-8 *-
def break_words(stuff):
    """This funtion will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_frist_word(words):
    """Prints the frist word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_setence(setence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(setence)
    return sort_words(words)

def print_first_and_last(setence):
    """Prints the first and last words of the setence"""
    words = break_words(setence)
    print_frist_word(words)
    print_last_word(words)

def print_first_and_last_sorted(setence):
    """Sorts the words then prints the first and last one."""
    words = sort_setence(setence)
    print_frist_word(words)
    print_last_word(words)