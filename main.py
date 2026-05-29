import json

FILE = "books.json"

def load_books():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_books(books):
    with open(FILE, "w") as f:
        json.dump(books, f)

def add_book(books):
    title = input("Book title: ")
    author = input("Author: ")
    rating = float(input("Rating (0-10): "))

    books.append({
        "title": title,
        "author": author,
        "rating": rating
    })

    print("📚 Book added!")

def show_books(books):
    if not books:
        print("No books yet.")
        return

    for i, b in enumerate(books, 1):
        print(f"{i}. {b['title']} by {b['author']} - ⭐ {b['rating']}")

def average_rating(books):
    if not books:
        print("No ratings yet.")
        return

    avg = sum(b["rating"] for b in books) / len(books)
    print(f"📊 Average rating: {avg:.2f}/10")

books = load_books()

while True:
    print("\n📚 BOOK TRACKER")
    print("1. Add book")
    print("2. View books")
    print("3. Average rating")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_book(books)
        save_books(books)

    elif choice == "2":
        show_books(books)

    elif choice == "3":
        average_rating(books)

    elif choice == "4":
        break