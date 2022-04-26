# json_dao.py
# stephen fitzsimon
# a class for accessing a json file that holds book db information

import json
import os

BOOK_format = {
    'title': None,
    'last_name': None,
    'first_name': None,
    'genre': None
}

class DAO():

    def __init__(self):
        self.books_list = self._load_books_file()

    def _load_books_file(self):
        ''' access and load the books in the save file'''
        # check if file exists, load the information, otherwise
        # return an empty list.
        if os.path.exists('books_json.json'):
            with open('books_json.json', 'r') as f:
                books = json.load(f)
        else:
            books = list()
        return books

    def _update_books_list(self):
        '''update the list of books and save to the json file
        returns true if successful save'''
        with open('books_json.json', 'w') as f:
            json_dump = json.dumps(self.books_list)
            f.write(json_dump)
        return True
    
    def add_book(self, book):
        '''add a book to the book list'''
        self.books_list.append(book)
        if self._update_books_list():
            return True
        else:
            return False