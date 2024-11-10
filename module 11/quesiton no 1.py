class Publication:
    numbering = 0

    def __init__(self, name):
        Publication.numbering += 1
        self.number = Publication.numbering
        self.name = name

    def print_information(self):
        print(f"{self.number}: {self.name}:")

class Magazine(Publication):

    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}, Type- Magazine")

class Book(Publication):

    def __init__(self, name, author, pg_count):
        self.author = author
        self.pg_count = pg_count
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}, Page Count: {self.pg_count}, Type- Book")

# Creating a library of publications
library = []
library.append(Magazine("Donald Duck", "Aki Hyyppä"))
library.append(Book("Compartment No. 6", "Rosa Liksom", 192))

# Print information of all publications in library
print("All Publications:")
for publication in library:
    publication.print_information()

# Print only books
print("\nBooks in library:")
for publication in library:
    if isinstance(publication, Book):
        publication.print_information()

# Print only magazines
print("\nMagazines in library:")
for publication in library:
    if isinstance(publication, Magazine):
        publication.print_information()
