# operations.py

# Data structures
books = {}
members = []
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "History")

# Core Functions
def add_book():
    isbn = input("Enter ISBN: ").strip()
    if isbn in books:
        print("Book with this ISBN already exists.")
        return
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    genre = input(f"Enter genre {genres}: ").strip()
    if genre not in genres:
        print("Invalid genre.")
        return
    try:
        total_copies = int(input("Enter total copies: "))
    except ValueError:
        print("Invalid number.")
        return

    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available": total_copies
    }
    print("Book added successfully.")


def add_member():
    member_id = input("Enter member ID: ").strip()
    if any(m["member_id"] == member_id for m in members):
        print("Member with this ID already exists.")
        return
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    members.append({"member_id": member_id, "name": name, "email": email, "borrowed_books": []})
    print("Member added successfully.")


def search_books():
    keyword = input("Enter title or author to search: ").strip().lower()
    found = False
    for isbn, book in books.items():
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print(f"{isbn}: {book['title']} by {book['author']} ({book['genre']}) - {book['available']} available")
            found = True
    if not found:
        print("No books found.")


def update_book():
    isbn = input("Enter ISBN to update: ").strip()
    if isbn not in books:
        print("Book not found.")
        return
    print("Leave blank to keep current value.")
    title = input(f"New title ({books[isbn]['title']}): ").strip() or books[isbn]['title']
    author = input(f"New author ({books[isbn]['author']}): ").strip() or books[isbn]['author']
    genre = input(f"New genre {genres} ({books[isbn]['genre']}): ").strip() or books[isbn]['genre']
    if genre not in genres:
        print("Invalid genre.")
        return
    books[isbn].update({"title": title, "author": author, "genre": genre})
    print("Book updated successfully.")


def update_member():
    member_id = input("Enter member ID to update: ").strip()
    for member in members:
        if member["member_id"] == member_id:
            print("Leave blank to keep current value.")
            name = input(f"New name ({member['name']}): ").strip() or member["name"]
            email = input(f"New email ({member['email']}): ").strip() or member["email"]
            member.update({"name": name, "email": email})
            print("Member updated successfully.")
            return
    print("Member not found.")


def delete_book():
    isbn = input("Enter ISBN to delete: ").strip()
    if isbn not in books:
        print("Book not found.")
        return
    for member in members:
        if isbn in member["borrowed_books"]:
            print("Cannot delete. Book currently borrowed.")
            return
    del books[isbn]
    print("Book deleted successfully.")


def delete_member():
    member_id = input("Enter member ID to delete: ").strip()
    for member in members:
        if member["member_id"] == member_id:
            if member["borrowed_books"]:
                print("Cannot delete. Member has borrowed books.")
                return
            members.remove(member)
            print("Member deleted successfully.")
            return
    print("Member not found.")


def borrow_book():
    member_id = input("Enter member ID: ").strip()
    isbn = input("Enter ISBN of book to borrow: ").strip()

    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        print("Member not found.")
        return
    if isbn not in books:
        print("Book not found.")
        return
    if len(member["borrowed_books"]) >= 3:
        print("Borrow limit reached (3 books).")
        return
    if books[isbn]["available"] <= 0:
        print("No copies available.")
        return

    member["borrowed_books"].append(isbn)
    books[isbn]["available"] -= 1
    print("Book borrowed successfully.")


def return_book():
    member_id = input("Enter member ID: ").strip()
    isbn = input("Enter ISBN of book to return: ").strip()

    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        print("Member not found.")
        return
    if isbn not in member["borrowed_books"]:
        print("This member didn't borrow that book.")
        return

    member["borrowed_books"].remove(isbn)
    books[isbn]["available"] += 1
    print("Book returned successfully.")
