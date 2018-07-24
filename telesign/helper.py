#!/usr/bin/env python

"""
A helper module to get anagram, palindrome of given strings and check string format
"""


def check_if_palindrome(word):
    """
    Function to check if given word is palindromic or not
    :return: bool
    """
    return word == word[::-1]


def are_anagram(word1, word2):
    """
    Function to check if pair of input words are anagram or not
    :param word1: str
    :param word2: str
    :return: bool
    """
    return sorted(word1) == sorted(word2)


def get_total_anagram_count(word_list=None):
    """
    Function to return the total number of anagrams in provided list
    :param word_list: list of str
    :return: int
    """
    seen = []
    anagram_count = 0
    # ["eat", "tea", "tan", "ate", "nat", "bat"]
    # ["aet", "aet", "ant", "aet", "ant", "abt"]

    for i in range(len(word_list)):
        if ''.join(sorted(word_list[i])) not in seen:
            j = i + 1
            while j < len(word_list):
                if sorted(word_list[i]) != sorted(word_list[j]):
                    j += 1
                else:
                    anagram_count += 1
                    seen.append(''.join(sorted(word_list[i])))
                    break

    return anagram_count


def get_anagram(query_word, word_list):
    """
    Function to return list of words in word_list that are anagram of query_word
    :param: query_word str word_list list
    :return: anagram_list list
    """
    anagram_list = [x for x in word_list if sorted(query_word) == sorted(x)]
    return anagram_list


def check_word_length(word):
    """
    Function to check if length of word is less than 4
    :return: bool
    """
    return len(word) < 4


def check_word_letters(word):
    """
    Function to check of letters in the word are lower case ascii between a-z
    :return: bool
    """
    return word.isalpha() and word.islower()

