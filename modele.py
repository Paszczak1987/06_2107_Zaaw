class Author:
    next_id = 1
    
    def __init__(self, first_name, last_name):
        self.id = Author.next_id
        Author.next_id += 1
        self.first_name = first_name
        self.last_name = last_name
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Book:
    next_id = 1
    
    def __init__(self, title, author):
        self.id = Book.next_id
        Book.next_id += 1
        self.title = title
        self.author = author
        
    def __str__(self):
        return f'{self.author} - {self.title}'
    
