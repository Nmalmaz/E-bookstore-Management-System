# This class stores a list of e-books and manages them
class Catalog:
    def __init__(self):
        self.__ebooks=[] # An empty list to store e-books
# Method to add an e-book to the catalog
    def add_ebook(self, ebook):
        self.__ebooks.append(ebook)
# Method to get an e-book by its position in the list
    def get_ebook_by_index(self, index):
        if 0 <= index < len(self.__ebooks):
            return self.__ebooks[index]
        return None
# Method to find an e-book by its title
    def get_ebook_by_title(self, title):
        for ebook in self.__ebooks:
            if ebook.get_title().lower() == title.lower():
                return ebook
        return None
# Method to display all e-books in the catalog
    def display_catalog(self):
        print("Available E-books:")
        for idx, ebook in enumerate(self.__ebooks):
            print(f"{idx + 1}. {ebook}")
# Method to search for e-books by genre
    def search_by_genre(self, genre):
        return [ebook for ebook in self.__ebooks if genre.lower() in ebook.__str__().lower()]