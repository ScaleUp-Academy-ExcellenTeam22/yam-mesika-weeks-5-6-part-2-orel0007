import itertools


def interleave(*mutable_object_args):
    """
    The function get mutable objects and chain them to a list by each object
    example: interleave('abc', [1, 2, 3], ('!', '@', '#')) -> ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
    :param mutable_object_args: collection of string, list, tuple.
    :return: list of all args chain
    """
    return list(itertools.chain.from_iterable(zip(*mutable_object_args)))


def generator_interleave(*args):
    """
    Creates a generator that yields each item from the return value of interleave(*args)
    :param args:
    :return: yield each object from list
    """
    list_chain_args = interleave(*args)
    for item in list_chain_args:
        yield item


if __name__ == "__main__":
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    gen = generator_interleave('abc', [1, 2, 3], ('!', '@', '#'))
    for i in gen:
        print(type(i))
        print(i)



