class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        self.author = author
        self.chapter = []

    def addchapter(self, chapter):
        self.chapter.append(chapter)

    def getbookPagecount(self):
        result = 0
        for ch in self.chapter:
            result += ch.pagecount
        return result


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} and  {self.lname}"


class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


author1 = Author("Martin", "Smith")

b1 = Book("War and Peace", 39.0, author1)

b1.addchapter(Chapter("Chapter 1", 122))
b1.addchapter(Chapter("Chapter 2", 1252))

print(b1.author)
print(b1.title)
print(b1.getbookPagecount())
