import os
import csv
from book import Book

class DAO:
    FILENAME = 'books_csv.csv'

    def __init__(self):
        '''make the book list and populate it from file'''
        #load the book data from the file
        self.book_list = self.load_book_file()
        #save the file just in case
        self.save_book_file()

    def load_book_file(self):
        '''loads the list of books from file, converts them into 
        book objects and appends the book objects to the book_list'''
        books = []
        #check if the file exists
        if os.path.isfile(self.FILENAME): 
            #since it exists, read it
            with open(self.FILENAME, 'r') as f:
                #make a reader object
                csv_reader = csv.reader(f)
                #read each row in the csv file using the reader object
                for row in csv_reader:
                    #make book objects and append them to the list of books
                    books.append(Book(row[0], row[1], row[2]))
        #return the list of books
        return books

    def save_book_file(self):
        '''saves the books to the file after deconverting them
        to a list object
        This is called everytime the book_list has changed'''
        books = [] #holds the lists that contain book information
        for book in self.book_list:
            #extract information from the book objects
            title = book.title
            author = book.author
            genre = book.genre
            #append to the list
            books.append([title, author, genre])
        with open(self.FILENAME, 'w') as f:
            #make a writer object for the file
            csv_writer = csv.writer(f)
            #write the list of list
            csv_writer.writerows(books)
    
    def add_book(self, book):
        '''append a book to the book list and then update the file'''
        self.book_list.append(book)
        self.save_book_file()
    
    def delete_book(self, book):
        '''remove a book from the book list and update the file'''
        self.book_list.remove(book)
        self.save_book_file()

    def update_book(self, book_old, book_new):
        pass 

if __name__ == '__main__':
    dao_obj = DAO()
    #create a bunch of books
    for x in range(10):
        title = f"title{x}"
        author = f"author{x}"
        genre = f"genre{x}"
        dao_obj.add_book(Book(title, author, genre))