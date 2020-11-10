books=["Harry Potter","Jungle Me Mangal","Jumanji"]
class Library:
    borrowed_books=[]
    def lend(self):
        for index,item in enumerate(books):print(f"[{index}]:",item)
        while True:
            inp=int(input("Enter the number of the book: "))
            if inp!="":break
        if inp <= len(books):self.borrowed_books.append(books[inp])
        else:print("Denied")
    def Return(self,name):
        if name in self.borrowed_books:self.borrowed_books.remove(name)
        else:print(f"You have not borrowed the book with the name {name}")
    @staticmethod
    def donate(name:str):books.append(name)