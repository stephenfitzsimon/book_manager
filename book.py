class Book:

    def __init__(self, user_input, from_file = False):
        #print(f"book_obj got {user_input}")
        if from_file:
            print(f'loading from file: {user_input}')
            self.title = user_input['title']
            self.author_name = user_input['author']
            self.genre = user_input['genre']
        else:
            self.title = self._clean_title(user_input)
            self.author_name = self._clean_author_name(user_input)
            self.genre = self._clean_genre(user_input)
            self.book_string = self._make_book_string()

    def _clean_title(self, user_input):
        if len(user_input.title) == 1:
            return user_input.title[0]
        else:
            return ' '.join(user_input.title)

    def _clean_author_name(self, user_input):
        if len(user_input.author) == 1:
            return user_input.author[0]
        else:
            return ' '.join(user_input.author)

    def _clean_genre(self, user_input):
        if len(user_input.genre) == 1:
            return user_input.genre[0]
        else:
            return ' '.join(user_input.genre)

    def _make_book_string(self):
        '''returns a formatted book string'''
        book_string = f"{self.title} \t {self.author_name} \t {self.genre}"
        return book_string

    def get_author_names(self):
        '''
        returns a tuple that includes the author first and last name,
        plus middle name if included, all in an ordered tuple
        '''
        names = self.author_name.split(' ')
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
            'author':self.author_name,
            'genre':self.genre
        }
        return book_dict