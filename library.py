class Library:
    libraryName = "National Library"
    def __init__(self, no_of_books, books):
        self.no_of_books = no_of_books  # integer
        self.books = books              # list

    def issueBook (self, books):
        self.no_of_books -= len(books)
        self.books = list (set(self.books) - set(books))
    def returnBook (self, books):
        self.no_of_books += len(books)
        self.books = self.books + books
        
    def compare (self, no_of_books, books):
        return True if no_of_books == len (books) else False

lib1 = Library (3, ["Phy", "Chem", "Bio"])
lib1.issueBook (["Bio"])
print (lib1.no_of_books)  
print (lib1.books)
lib1.returnBook (["Math", "English", "Urdu"])
print (lib1.no_of_books)  
print (lib1.books)
print (lib1.compare(lib1.no_of_books, lib1.books))
# The End