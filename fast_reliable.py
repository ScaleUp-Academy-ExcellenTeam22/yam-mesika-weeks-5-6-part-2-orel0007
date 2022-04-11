from datetime import datetime


def timeit(func):
    """
    This function is a decorator to check the time running of a function.
    :param func: decorator on a given function
    :return: wrapper_function decorator
    """
    def wrapper_function(*args):
        start = datetime.now()
        func(*args)
        end = datetime.now()
        print(f" Run time of the function {func.__name__} with {type(*args)} is: {end - start}.")
    return wrapper_function


def build_list_and_set_words(file_name):
    """
    :param file_name:
    :return: 1) list of the words in the file, 2)set of the words in the file
    """
    list_words = List = open(file_name).readlines()
    set_words = set(list_words)
    return list_words, set_words


@timeit
def average_runtime(iterable_object):
    """

    :param iterable_object: iterable_object holds 
    :return:
    """
    for i in range(1000):
        if "zwitterion" in iterable_object:
            pass


if __name__ == "__main__":
    words_list, words_set = build_list_and_set_words("words.txt")
    average_runtime(words_list)
    average_runtime(words_set)





