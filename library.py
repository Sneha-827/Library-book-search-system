# Library Book Search System

def search_book():
    name = input("Enter book name: ")

    file = open("books.txt", "r")

    found = False

    for line in file:
        book = line.strip().split(",")

        if book[0].lower() == name.lower():
            print("\nBook Found")
            print("Name:", book[0])
            print("Author:", book[1])
            print("Price: ₹", book[2])

            found = True
            break

    file.close()

    if found == False:
        print("Book not found")


def display_books():
    file = open("books.txt", "r")

    print("\nBooks Available:")

    for line in file:
        book = line.strip().split(",")
        print(book[0])

    file.close()


while True:
    print("\n--- Library Search System ---")
    print("1. Search Book")
    print("2. Display Books")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        search_book()

    elif choice == 2:
        display_books()

    elif choice == 3:
        print("Thank you")
        break

    else:
        print("Invalid choice")