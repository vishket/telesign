#!/usr/bin/env python

"""
RESTful service to manage collection of words

Supported endpoints

POST /words
GET /words/<word>
GET /words/count
DELETE /words/<word>
DELETE /words
GET /palindromes/count
GET /anagrams/count
GET /anagrams/<word>

"""

from flask import Flask, jsonify, request, abort
from telesign import helper
from telesign.database import Database


app = Flask(__name__)


@app.route('/v1/words/<word>', methods=['GET'])
def get_word(word):
    """
    Function to return the word if it is present in the collection
    :return: word str
    """
    dbconn = Database()
    dbconn.select_all()
    for record in dbconn.cursor:
        if record[0] == word:
            return str(word)
    return abort(404)


@app.route('/v1/words', methods=['POST', 'DELETE'])
def words():
    """
    Function to support /words endpoint.
    Adds words to collection if HTTP verb is POST
    Deletes all words in collection of HTTP vers is DELETE
    :return: bool
    """
    dbconn = Database()
    collection = []

    dbconn.select_all()

    # Get a list of all existing words
    for record in dbconn.cursor:
        collection.append(record[0])

    if request.method == 'POST':
        raw_data = request.get_json()
        for word in set(raw_data):
            if word not in collection:
                # Check if word length is less than or equal to 4 and all characters are ascii a-z
                word_size_check = helper.check_word_length(word)
                word_letter_check = helper.check_word_letters(word)
                if word_size_check and word_letter_check:
                    dbconn.insert_data(word)
        dbconn.select_all()
        return jsonify(dbconn.cursor.fetchall())

    if request.method == 'DELETE':
        dbconn.delete_all_data()
        dbconn.select_all()
        return jsonify(dbconn.cursor.fetchall())


@app.route('/v1/words/count', methods=['GET'])
def get_words_count():
    """
    Function to return count of unique words in collection
    :return: word_count str
    """
    dbconn = Database()

    dbconn.select_all()
    word_count = dbconn.cursor.rowcount
    return str(word_count)


@app.route('/v1/words/<word>', methods=['DELETE'])
def delete_word(word):
    """
    Function to delete provided word from collection
    :param word:
    :return: json obj of collection
    """
    dbconn = Database()

    dbconn.delete_data(word)
    dbconn.select_all()
    return jsonify(dbconn.cursor.fetchall())


@app.route('/v1/palindromes/count', methods=['GET'])
def get_palindrome_count():
    """
    Function to return number of palindromic words in data store
    :return: palindrome_count str
    """
    dbconn = Database()
    palindrome_count = 0

    dbconn.select_all()

    for record in dbconn.cursor:
        if helper.check_if_palindrome(record[0]):
            palindrome_count += 1
    return str(palindrome_count)


@app.route('/v1/anagrams/<word>')
def get_anagrams(word):
    """
    Function to check for anagrams of word provided
    :return: anagram_list list
    """
    dbconn = Database()

    anagram_list = []
    collection = []

    # Get all words in collection and store in a list
    dbconn.select_all()
    for record in dbconn.cursor:
        collection.append(record[0])

    if len(collection) > 0:
        anagram_list = helper.get_anagram(word, collection)
    return jsonify(anagram_list)


@app.route('/v1/anagrams/count')
def get_total_anagrams():
    """
    Function to return number of anagrams in data store
    :return: anagram_count: str
    """
    dbconn = Database()

    anagram_count = 0
    collection = []

    # Get all words in collection and store in a list
    dbconn.select_all()
    for record in dbconn.cursor:
        collection.append(record[0])

    if len(collection) > 0:
        anagram_count = helper.get_total_anagram_count(collection)
    return str(anagram_count)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)