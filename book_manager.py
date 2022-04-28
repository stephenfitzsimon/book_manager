# book_manager.py
# stephen fitzsimon
# a CLI program for keeping a personal library

import argparse
import json
import json_dao

BOOKS = json_dao.DAO()

def main():
    '''handles the control flow of the program'''
    user_input = read_user_input()
    print(user_input)
    book = new_book(user_input.title, user_input.author, user_input.genre)
    print(BOOKS.add_book(book))

def read_user_input():
    '''handles user CLI input'''
    parser = argparse.ArgumentParser(
        description = 'manages a personal library'
    )
    parser.add_argument(
        '-t',
        '--title',
        nargs = '+',
        type = str,
        action = 'append',
        help = 'book title'
    )
    parser.add_argument(
        '-a',
        '--author',
        nargs = '+',
        type = str,
        action = 'append',
        help = 'book author'
    )
    parser.add_argument(
        '-g',
        '--genre',
        nargs = '+',
        type = str,
        action = 'append',
        help = 'book genre'
    )
    return parser.parse_args()

def new_book(title, author, genre):
    '''add a book to the database
        Args:
            title (str) = book title
            author (str) = book author
            genre (str) = book genre
    '''
    book = {
        'title' : ' '.join(title[0]),
        'first_name' : author[0],
        'last_name' : author[0],
        'genre' : ' '.join(genre[0])
    }
    return book 

def return_book_string(book):
    '''Returns a formatted string for a book
        Args:
            book (book) = a book dictionary
    '''
    book_string = f"{book['title']} \t {book['last_name']}, {book['first_name']} \t {book['genre']}"
    return book_string

def print_books():
    for book in BOOKS:
        print(return_book_string(book))

if __name__=='__main__':
    main()