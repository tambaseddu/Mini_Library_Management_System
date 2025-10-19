# Library Management System

## Overview
A simple Python-based library system using dictionaries, lists, and tuples for managing books and members with CRUD, borrow, and return operations.

## Requirements
- Python 3.6 or higher

## Files Included
- operations.py: Core functions for CRUD operations, borrowing, and returning books.
- demo.py: Interactive menu-driven demo to test the system.
- tests.py: Unit tests to verify functionality.
- UML.png: Hand-drawn UML diagram showing data structures and functions.
- DesignRationale.pdf: Short design rationale (1 page explaining use of dictionary, list, tuple).

## Running the Code
1. Ensure Python 3.6+ is installed on your system.
2. Place all Python files (operations.py, demo.py, tests.py) in the same directory.
3. To run the interactive demo:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the files.
   - Execute: python demo.py
   - Follow the on-screen menu prompts to add books/members, search, borrow/return, etc.
4. To run the unit tests:
   - In the same directory, execute: python tests.py
   - Expected output: "All tests passed!" if everything works correctly.

## Example Usage in Demo
- Choose option 1 to add a book: Enter ISBN (e.g., 909), Title (e.g., Jack de Giant), Author (e.g., Richard), Genre (e.g., Fiction), Total Copies (e.g., 5).
- Choose option 2 to add a member: Enter ID (e.g., F5423), Name (e.g., Joseph Farmer), Email (e.g., josephfarmer@gmail.com).
- Choose option 8 to borrow: Enter Member ID (F5423) and ISBN (909) – succeeds if <3 books borrowed and copies available.
- Choose option 9 to return: Enter Member ID (F5423) and ISBN (909).
- Tests cover scenarios like invalid genres, duplicate IDs, borrowing limits, and deletion protections.

For issues, ensure no syntax errors in Python files. No external libraries required beyond standard Python.
