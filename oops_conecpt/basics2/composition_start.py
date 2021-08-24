class Book:
    def __init__(self,title,price,authorfname,authorlname):
        self.title = title
        self.price = price

# todo we can separate out 'Author' and 'chapter' into separate Entity
# todo we can use composition to extract and separate it
        self.authorfname =authorfname
        self.authorlname =authorlname

        self.chapter =[]

    def addchapter(self,name,pages):
        self.chapter.append((name,pages))

b1 = Book("War and Peace",39.0 , "Leo","Tolstoy")

b1.addchapter("Chapter 1",122)
b1.addchapter("Chapter 2",1252)

print(b1.title)