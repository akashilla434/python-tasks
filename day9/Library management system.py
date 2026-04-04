class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display(self):
        print("title:", self.title)
        print("author:",self.author)
class ebook(book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size = file_size
    def display(self):
        super().display()
        print("file size:", self.file_size,"mb")
ebook1 = ebook("python basics", "akash", 5)
ebook1.display()
