# user_input.py
# class manages making parsers with argparse and returns them to the program class

import argparse
import book_manager

class UserInput():

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog = "bookmanager",
            description = "book_manager manages a personal library"
        )
        self.subparsers = self.parser.add_subparsers(
            help = "sub-command help"
        )
        self.add_cmd_parser = self._make_add_cmd_parser()
        self.print_cmd_parser = self._make_print_cmd_parser()
        self.user_input = self._get_user_input()
    
    def __call__(self):
        return self.user_input
    
    def get_input(self):
        return self.user_input

    def _get_user_input(self):
        '''gets and returns user input'''
        return self.parser.parse_args()

    def _make_add_cmd_parser(self):
        '''makes the add command which allows for adding a book
        to the file'''
        add_cmd = self.subparsers.add_parser(
            'add',
            help = 'add a book to the manager'
        )
        add_cmd.add_argument(
            '-t',
            '--title',
            nargs = '+',
            type = str,
            help = 'book title'
        )
        add_cmd.add_argument(
            '-a',
            '--author',
            nargs = '+',
            type = str,
            help = 'book author'
        )
        add_cmd.add_argument(
            '-g',
            '--genre',
            nargs = '+',
            type = str,
            help = 'book genre'
        )
        add_cmd.set_defaults(func=book_manager.add_book)
        return add_cmd

    def _make_print_cmd_parser(self):
        '''makes the print command which prints all the books
        in the file'''
        print_cmd = self.subparsers.add_parser(
            'print',
            help = 'print out all books entered into the program'
        )
        print_cmd.add_argument(
            '-l',
            '--list',
            type=int,
            nargs = '?',
            default=5,
            help = 'number of records to print'
        )
        print_cmd.set_defaults(func=book_manager.print_books)
        return print_cmd

if __name__=='__main__':
    user_input = UserInput()
    print(user_input.user_input)