# json_dao.py
# stephen fitzsimon
# a class for accessing a json file that holds book db information

import json
import os
from book import Book

class DAO():

    def __init__(self):
        self.books_list = self._load_books_file()

    def get_books_list(self):
        return self.books_list

    def _load_books_file(self):
        ''' access and load the books in the save file'''
        # check if file exists, load the information, otherwise
        # return an empty list.
        if os.path.exists('books_json.json'):
            print('file found')
            books = []
            with open('books_json.json', 'r') as f:
                books = json.load(f)
            for book_dict in books:
                book_obj = Book(book_dict, from_file=True)
                books.append(book_obj)
        else:
            print('No file found')
            books = []
        return books

    def _update_books_list(self):
        '''update the list of books and save to the json file
        returns true if successful save'''
        with open('books_json.json', 'w') as f:
            json_dump = json.dumps(self.books_list)
            f.write(json_dump)
        return True

    def _save_books_list(self):
        try:
            with open('books_json.json', 'w') as f:
                json_dump = json.dumps(self.books_list)
                f.write(json_dump)
            return True
        except:
            return False
    
    def add_book(self, book):
        '''add a book to the book list'''
        self.books_list.append(book.make_book_dictionary())
        if self._save_books_list():
            return True
        else:
            return False

if __name__=='__main__':
    dao_obj = DAO()
    print(dao_obj.books_list)
    dao_obj._save_books_list()