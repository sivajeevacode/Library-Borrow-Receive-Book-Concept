 
class user:
    def __init__(self,books):
        self.books=books
        
    def list_book(self):
        print("Available Books")
        for i in self. books:
            print(i)
            
    def borrow_book(self,borrow_book):
        if borrow_book in self.books:
            print("Get Your Book Now")
            self.books.remove(borrow_book)
            
        else:
            print("Book Not Available")
            
    def receive_book(self,receive_book):
        print("You Receive Book")
        self.books.append(receive_book)
        
        
books=["Java","Python","Javascript","C"]

library=user(books)

msg=""" 
    1.Select Book
    2.Borrow Book
    3.Receive Book
    
    """
    
while True:
    print(msg)
    a=int(input("Enter Your Choice : "))
    
    if a==1:
        library.list_book()
        
    elif a==2:
        book=input("Enter Your Borrow Book Name:")
        library.borrow_book(book)
        
    elif a==3:
        book=input("Enter Your Receive Book Name:")
        library.receive_book(book)
        
    else:
        print("Thank You Come Again! ")
        quit()
    
    
    
