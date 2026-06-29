def search_book():
    name = input("Enter book name: ")

    file = open("books.txt", "r")

    found = False   #a variable to know if book is found or not.  Let's consider it as false at first

    for line in file:
        book = line.strip().split(",") #splits the sentece at "," and stores it in a list in order

        if book[0].lower() == name.lower():    #covert the text into lower so it wont affect the comparision
            print("\nBook Found")
            print("Name:", book[0])
            print("Author:", book[1])
            print("Price: ₹", book[2])

            found = True   # True if the book is found
            break

    file.close()

    if found == False:
        print("Book not found")

#search book using author's name
def search_author():
    author = input("Enter the Author's name: ")

    file = open("books.txt",  "r")

    found = False

    for line in file:
        book = line.strip().split(",")

        if book[1].lower() == author.lower():
            print("\nBook Found")
            print("Name:", book[0])
            print("Author:", book[1])
            print("Price: ₹", book[2])

            found = True
            break

    file.close()

    if found == False:
        print("Book not found")
            


#displaying all available books
def display_books(): 
    file = open("books.txt", "r")

    print("\nBooks Available:")

    for line in file:
        book = line.strip().split(",")
        print(book[0])

    file.close()


while True:
    print("\n--- Library Search System ---")
    print("1. Search Book by name of the book")
    print("2. Search Book by Author's name")
    print("3. Display all the Books")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        search_book()

    elif choice == 2:
        search_author()

    elif choice == 3:
        display_books()

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Invalid choice") 