# Library Management System (Constructor & Inheritance)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display(self):
        super().display()
        print("File Size:", self.file_size, "MB")

e = EBook("Python Basics", "John", 5)

e.display()
