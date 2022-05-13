class Book():

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def get_book_string(self):
        '''returns a formatted book string'''
        book_string = f"{self.title} \t {self.author} \t {self.genre}"
        return book_string

    def get_author_names(self):
        '''
        returns a tuple that includes the author first and last name,
        plus middle name if included, all in an ordered tuple
        '''
        names = self.author.split(' ')
        if len(names) == 2:
            return (names[0], names[1])
        elif len(names) == 3:
            return (names[0], names[1], names[2])
        else:
            return (names[0])
    
    def make_book_dictionary(self):
        '''returns a dictionary of the book object'''
        book_dict = {
            'title':self.title,
            'author':self.author,
            'genre':self.genre
        }
        return book_dict