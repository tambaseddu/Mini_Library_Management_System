# demo.py
import operations as op


def main():
    while True:
        print("\n*** Library Management System ***")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Update Member")
        print("6. Delete Book")
        print("7. Delete Member")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            op.add_book()
        elif choice == "2":
            op.add_member()
        elif choice == "3":
            op.search_books()
        elif choice == "4":
            op.update_book()
        elif choice == "5":
            op.update_member()
        elif choice == "6":
            op.delete_book()
        elif choice == "7":
            op.delete_member()
        elif choice == "8":
            op.borrow_book()
        elif choice == "9":
            op.return_book()
        elif choice == "10":
            print("BYE-BYE, TENKI!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
