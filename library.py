def search_book():
    name = input("Enter book name: ")

    file = open("books.txt", "r")

    found = False   #a variable to know if book is found or not.  Let's consider it as false at first
    
    # list to store related books
    related=[]

    #if the name matches the user entered name
    for line in file:
        
        book = line.strip().split(",") #splits the sentece at "," and stores it in a list in order

        if book[0].lower() == name.lower():    #covert the text into lower so it wont affect the comparision
            print("\nBook Found")
            print("Name:", book[0])
            print("Author:", book[1])
            print("Price: Rs.", book[2])

            found = True   # True if the book is found
            break

        #if the name doesnt match and any of the keyword  matches (Partial match)
        elif name.lower() in book[0].lower(): 
            related.append(book[0])      

    file.close()

    if found == False:
        print("Book not found")
        print("Related books:")
        for i in related:
            print("\t", i)

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
            print("Price: Rs.", book[2])
            print("\n")

            found = True

    file.close()

    if found == False:
        print("Book not found")

#Search book by the cost range
def search_cost():
    min_cost = int(input("Enter the minimum book cost: "))
    max_cost = int(input("Enter the maximum book cost: "))

    file = open("books.txt", "r")

    found = False

    print("\n Books that are in price range: ")
    for line in file:
        book = line.strip().split(",")

        #the price in txt file is stored as string so we use int() to convert it into integer
        amount = int(book[2])

        if min_cost <= amount <= max_cost:
            print(book[0], "-Rs.", book[2])
            found=True

    file.close()
    
    if found == False:
        print("No books found in this price range")



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
    print("3. Search Book by cost range")
    print("4. Display all the Books")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        search_book()

    elif choice == 2:
        search_author()

    elif choice == 3:
        search_cost()

    elif choice == 4:
        display_books()

    elif choice == 5:
        print("Thank you")
        break

    else:
        print("Invalid choice") 