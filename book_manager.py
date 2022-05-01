# book_manager.py
# stephen fitzsimon
# a CLI program for keeping a personal library

import argparse
import json
from json_dao import DAO
import userinput
import book

DAO_OBJECT = DAO()
print(f'loaded: {DAO_OBJECT.books_list}')

def main():
    '''handles the control flow of the program'''
    input_obj = userinput.UserInput()
    user_in = input_obj.get_input()
    # print(user_in)
    input_obj.user_input.func(user_in)

def add_book(user_in):
    '''add a book to the database
        Args:
            user_in (namespace obj) = user arguments from CLI input
    '''
    book_obj = book.Book(user_in)
    DAO_OBJECT.add_book(book_obj)

def print_books(user_in):
    book_list = DAO_OBJECT.get_books_list()
    if type(book_list) == None:
        print('There are no books on file')
    elif user_in.list < len(book_list):
        for i in range(user_in.list):
            print(book_list[i].book_string)
    else:
        for i in range(len(book_list)):
            print(book_list[i].book_string)


if __name__=='__main__':
    main()
    pass