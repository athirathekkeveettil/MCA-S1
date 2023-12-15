# create a class Publisher(name),derive a class Book(title,author) from Publisher.
# derive a class Python(price,no.of pages) from Book.
# write a program that displays information about a Python Book,use base class constructor invoking and method overridding.

class Publisher:
    def.__init.__(self,name):
        self.name=name
    def display(self):
        print("Publisher:",self.name)
class Book(Publisher):
    def__init__(self,title,author,name):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        super display()
        print("Title:",self.title)
        print("Author:",self.author)
class Python(Book):
    def__init__(self,title,author,name,price,n):
        super()__init__(title,author,name
        self.price=price
        self.n=n
    def display(self):
        super().display()
        print("Price:",self.price)
        print("Number of  pages:",self.n)

a=Python("Python Programming","BalaguruSwamy","AR Publications",500.0,500)
a.display()
