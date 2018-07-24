#!/usr/bin/env python

import unittest

# Local import
from telesign import helper


class TestHelper(unittest.TestCase):
    """
    Tests for Helper functions
    """
    def test_check_palindrome(self):
        """
        Test to validate that "kayak" is a palindrome
        :return:
        """
        is_palindrome = helper.check_if_palindrome("kayak")
        assert is_palindrome is True

    def test_check_not_palindrome(self):
        """
        Test to validate that "telesign" is a NOT palindrome
        :return:
        """
        is_palindrome = helper.check_if_palindrome("telesign")
        assert is_palindrome is False

    def test_get_total_anagram_count(self):
        """
        Test to return total number of anagrams in a list of words
        :return:
        """
        word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
        anagram_count = helper.get_total_anagram_count(word_list)
        assert anagram_count == 2

    def test_get_anagram(self):
        """
        Test if list contains anagram of provided word
        :return:
        """
        word = "abt"
        word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
        anagram_list = helper.get_anagram(word, word_list)

        assert len(anagram_list) == 1

    def test_check_word_length(self):
        """
        Test to check if length of word is less than 4
        :return:
        """
        word = "telesign"
        word_len = helper.check_word_length(word)

        assert word_len is False



