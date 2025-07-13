class ItemNotFound(Exception):
    pass
class LibraryItem:
    id_counter = 0
    def __init__(self, id, title):
        if title == None:
            raise ValueError("Title not must prazen")
        self._id = id
        self._title = title

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @classmethod
    def id_generate(cls, *args, **kwargs):
        LibraryItem.id_counter += 1
        return cls(LibraryItem.id_counter, *args, **kwargs)

    def print_details(self):
        return f"{self.id}: {self.title}"

class Book(LibraryItem):
    def __init__(self, id, title, author, page_count, publication_year):
        super().__init__(id, title)
        self._author = author
        self.page_count = page_count
        self.publication_year = publication_year

    @property
    def author(self):
        return self._author

    @property
    def page_count(self):
        return self._page_count

    @property
    def publication_year(self):
        return self._publication_year

    @page_count.setter
    def page_count(self, value):
        if not 0 < value <= 5000:
            raise ValueError("Invalid page count")
        self._page_count = value

    @publication_year.setter
    def publication_year(self, value):
        if value < 1450 or value > 2025:
            raise ValueError("Invalid year: enter 1450-2025")
        self._publication_year = value

    def print_details(self):
        library_item_ov = super().print_details()
        return library_item_ov + f"{self.author} {self.page_count} {self.publication_year}"

class Magazine(LibraryItem):
    month = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    def __init__(self, id, title, issue_number, publication_month):
        super().__init__(id, title)
        self.valid_issue_number(issue_number)
        self.valid_month(publication_month)

    def valid_issue_number(self, issue_number):
        if issue_number < 0:
            raise ValueError("Error")
        self.issue_number = issue_number

    def valid_month(self, publication_month):
        if publication_month not in self.month:
            raise ValueError("Error")
        self.publication_month = publication_month

    def print_details(self):
        magaz_ov = super().print_details()
        return magaz_ov + f"{self.publication_month}, {self.issue_number}"

class Library:
    def __init__(self):
        self._list_items = []

    def add_item(self, item):
        for exist_id in self._list_items:
            if exist_id.id == item.id:
                raise ValueError("Error")
        self._list_items.append(item)
    def find_by_id(self, item_id):
        for item in self._list_items:
            if item.id == item_id:
                return item
        raise ItemNotFound(f"Item {item_id} not found")

    def remove_item(self, item_id):
        item = self.find_by_id(item_id)
        self._list_items.remove(item)

    def find_by_title(self, title):
        for item in self._list_items:
            if item.title == title:
                return item

    def list_all_items(self):
        for item in self._list_items:
            print(item.print_details())

    def borrow_item(self, member, item_id):
        if item_id in member.borrowed_items:
            raise ValueError("Erorr")
        member.borrowed_items.append(item_id)

    def return_item(self, member, item_id):
        if item_id not in member.borrowed_items:
            raise ValueError("Erorr")
        member.borrowed_items.remove(item_id)

class Member:
    def __init__(self, member_id, name):
        if member_id < 0:
            raise ValueError("Must be posivite number")
        if name is None:
            raise ValueError("Error")
        self.member_id = member_id
        self.name = name
        self.borrowed_items = []
    def list_borrowed_items(self):
        for items in self.borrowed_items:
            print(items)

    def __str__(self):
        return f"{self.name}, {self.member_id}, {self.borrowed_items}"


library = Library()
member = Member(1, "Ivan")

book1 = Book.id_generate("1984", "Orwell", 300, 1949)
book2 = Book.id_generate("Dune", "Herbert", 412, 1965)
magazine1 = Magazine.id_generate("Tech Today", 5, "June")

library.add_item(book1)
library.add_item(book2)
library.add_item(magazine1)

print("\nAll items in library:")
library.list_all_items()

print("\n Find by title:")
found = library.find_by_title("Dune")
if found:
    print(found.print_details())
else:
    print("Not found.")

library.borrow_item(member, book1.id)
print("\nBorrowed book IDs:")
print(member.borrowed_items)

try:
    library.borrow_item(member, book1.id)
except ValueError as e:
    print(f"\nError: {e}")

library.return_item(member, book1.id)
print("\nAfter return:")
print(member.borrowed_items)

print("\n Borrowed items:")
member.list_borrowed_items()


