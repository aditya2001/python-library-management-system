
class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} BOOKS ARE AVAILABLE: ")
        for book in self.books:
            print(book)
        print("\n")    
    
    
    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            print(
                f"{bookname} BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED.\n")
        else:
            track.append({name: bookname})
            print("BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN ON TIME.\n")
            self.books.remove(bookname)

    def returnBook(self, name, bookname):
            if {name: bookname} in track:
               track.remove({name: bookname})
               self.books.append(bookname)
               print("Book returned")
            else:
                print("Invalid entry")   

if __name__ == "__main__":

    Delhilibrary = Library(["English", "Hindi", "Science", "Maths", "History", "Social"])        
    track = []
    
    print("\t\t\t\t\t\t\t♦♦♦♦♦♦♦ WELCOME TO THE DELHI LIBRARY ♦♦♦♦♦♦♦\n")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Listing all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. exit the library\n""")
    
    while (True):

        response = int(input("Enter your choice: "))
        if response == 1:
          Delhilibrary.displayAvailableBooks()
        elif response == 2:
          Delhilibrary.borrowBook(
          input("Enter your name: "), input("Enter name of the book you want to borrow: "))
        elif response == 3:
          Delhilibrary.returnBook(
          input("Enter your name: "), input("Enter name of the book you want to return: "))
        elif response == 4:  # track
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")
            
        elif response == 5: #exit
                print("THANK YOU ! \n")
                exit()
        else:
                print("INVAILD INPUT! \n")              