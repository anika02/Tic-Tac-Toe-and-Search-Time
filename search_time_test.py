import random
import time
from binary_search_tree.btree import LinkedBST


def read_file(file_name):
    """ (str) -> list
    Read the file and return list with words """
    with open(file_name, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]


def create_binary_tree(words):
    """ (list) -> LinkedBST
    Return binary search tree with words of list with these words """
    tree = LinkedBST()
    for word in words:
        tree.add(word)
    return tree


def list_method(words_dict, random_words):
    """ (list, list) -> NoneType
    Find elements of random_words in words_dict"""
    for elem in random_words:
        if elem in words_dict:
            pass


def binary_tree_method(tree, random_words):
    """ (LinkedBST, list) -> NoneType
    Find elements of random_words in tree"""
    for elem in random_words:
        tree.find(elem)


def main():
    """ () -> ()
    The main function for definition the time
    of the different search methods """
    words_dict = read_file('words.txt')
    random_words = random.sample(words_dict, 1000)
    words_dict = words_dict[:991]

    times = time.time()
    list_method(words_dict, random_words)
    time_list = time.time() - times
    simple_tree = create_binary_tree(words_dict)

    times = time.time()
    binary_tree_method(simple_tree, random_words)
    time_simple_tree = time.time() - times

    shuffle_words = words_dict[:]
    random.shuffle(shuffle_words)
    random_tree = create_binary_tree(shuffle_words)

    times = time.time()
    binary_tree_method(random_tree, random_words)
    time_random_tree = time.time() - times

    simple_tree.rebalance()

    times = time.time()
    binary_tree_method(simple_tree, random_words)
    time_bal_tree = time.time() - times
    print(f"""\
List method:                        {time_list}
Simple binary tree method:          {time_simple_tree}
Random words binary tree method:    {time_random_tree}
Balanced binary tree method:        {time_bal_tree}""")


if __name__ == "__main__":
    main()
