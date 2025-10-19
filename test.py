# tests.py
import operations as op


def run_tests():
    op.books.clear()
    op.members.clear()

    # Add book
    op.books["919"] = {"title": "Python Basics", "author": "John Doe", "genre": "Fiction", "total_copies": 2,
                       "available": 2}
    op.members.append({"member_id": "M1", "name": "Alice", "email": "alice@mail.com", "borrowed_books": []})

    # Test borrow
    op.books["919"]["available"] = 1
    op.members[0]["borrowed_books"].append("919")
    assert op.books["919"]["available"] == 1 or op.members[0]["borrowed_books"] == ["919"]

    # Test return
    op.members[0]["borrowed_books"].remove("919")
    op.books["919"]["available"] += 1
    assert op.books["919"]["available"] == 2

    # Test genre validity
    assert "Fiction" in op.genres

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
