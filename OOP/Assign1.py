# Base class
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def read(self):
        print(f"You start reading '{self.title}' by {self.author}.")

    def book_info(self):
        print(f"'{self.title}' by {self.author} - {self.pages} pages - Genre: {self.genre}")

# Subclass (Inheritance)
class ComicBook(Book):
    def __init__(self, title, author, pages, genre, illustrator):
        super().__init__(title, author, pages, genre)
        self.illustrator = illustrator

    def read(self):
        print(f"You enjoy the colorful illustrations while reading '{self.title}' by {self.author}.")

    def comic_info(self):
        self.book_info()
        print(f"Illustrated by: {self.illustrator}")

# Main section to create objects and test the code
if __name__ == "__main__":
    # Create a Book object
    novel = Book("1984", "George Orwell", 328, "Dystopian")
    novel.book_info()
    novel.read()

    # Create a ComicBook object
    comic = ComicBook("Spider-Man", "Stan Lee", 120, "Superhero", "Steve Ditko")
    comic.comic_info()
    comic.read()