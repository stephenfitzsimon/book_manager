# user_input.py
# class manages making parsers with argparse and returns them to the program class

import argparse

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
        self.user_input = self._get_user_input()

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
            action = 'append',
            help = 'book title'
        )
        add_cmd.add_argument(
            '-a',
            '--author',
            nargs = '+',
            type = str,
            action = 'append',
            help = 'book author'
        )
        add_cmd.add_argument(
            '-g',
            '--genre',
            nargs = '+',
            type = str,
            action = 'append',
            help = 'book genre'
        )
        return add_cmd

    def _make_print_cmd_parser(self):
        '''makes the print command which prints all the books
        in the file'''
        return None